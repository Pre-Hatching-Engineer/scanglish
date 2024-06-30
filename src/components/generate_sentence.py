import streamlit as st
import os
import sys
from dotenv import load_dotenv

load_dotenv(override=True)
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定

from openai import OpenAI
from database import getWordsList, get_user_id

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def generateSentence_by_openai(words_list, difficulty, theme="一般的な話題"):
    system_prompt = """
    あなたはプロの通訳者です。
    """

    user_prompt = f"""
    次の形式で、オプションの英単語とテーマに基づいて英語と日本語の文章を生成してください。

    # 出力形式
    [英語の文章]
    ----------
    [日本語訳の文章]
    
    # オプション
    英単語リスト: {words_list}
    難易度: {difficulty}
    テーマ: {theme}
    

    # 制約
    - 文章の長さは単語の数によって適切に変えてください。
    - 文章の長さの範囲は、3から200単語です。
    - オプションの単語は必ず文章に含めてください。
    - なるべく自然な文章となるように心がけてください。
    - 質問で返さないこと
    - 出力に英単語リスト、難易度、テーマを含めないこと
    - 英単語リストの単語は「*」で囲ってください。
    """
    print(f"words_list: {words_list}")
    print(f"difficulty: {difficulty}")
    print(f"theme: {theme}")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
    )

    res_en = response.choices[0].message.content.split("----------")[0].strip()
    res_ja = response.choices[0].message.content.split("----------")[1].strip()

    return res_en, res_ja


def generateSentence():
    # セッションの初期化
    if "generated_sentence_en" not in st.session_state:
        st.session_state.generated_sentence_en = None
    if "generated_sentence_ja" not in st.session_state:
        st.session_state.generated_sentence_ja = None
    # ログインしてなければ何も表示しない
    if st.session_state.username is None:
        return
    # 2列で表示
    col1, col2 = st.columns(2)

    with col1:
        st.title("Generate Sentence")
        st.write("あなたの単語帳から文章を生成します。")

        length = st.selectbox("使用する単語数（必須）", [5, 10, 20])
        length_map = {"短い": 20, "並": 75, "長い": 200}
        difficulty = st.selectbox("難しさ（必須)", ["簡単", "普通", "難しい"])
        theme = st.text_input("テーマ")

        if st.button("生成"):
            if not length:
                st.warning("文章の長さを選択してください")
            elif not difficulty:
                st.warning("難しさを選択してください")
            else:
                # ここで単語を取ってくる
                user_id = get_user_id(st.session_state.username)
                words_list = getWordsList(user_id, length)
                if theme:
                    sentence_en, sentence_ja = generateSentence_by_openai(words_list, difficulty, theme)
                else:
                    sentence_en, sentence_ja = generateSentence_by_openai(words_list, difficulty)

                st.session_state.generated_sentence_en = sentence_en
                st.session_state.generated_sentence_ja = sentence_ja

    with col2:
        if st.session_state.generated_sentence_en is not None:
            st.text_area("Generated Sentence in English", st.session_state.generated_sentence_en, height=300)

            # トグルブロックとして日本語訳を表示
            if st.toggle("Show Japanese Translation"):
                # generated_sentence_ja
                st.text_area("Generated Sentence in Japanese", st.session_state.generated_sentence_ja, height=300)


if __name__ == "__main__":
    generateSentence()
