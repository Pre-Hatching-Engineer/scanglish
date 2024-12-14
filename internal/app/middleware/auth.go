package middleware

import (
	"fmt"
	"os"

	"github.com/golang-jwt/jwt/v5"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

var jwtSecret = []byte("local-secret-key")

type authClaims struct {
	Username string `json:"username"`
	jwt.RegisteredClaims
}

func AuthMiddleware() echo.MiddlewareFunc {
	return middleware.KeyAuthWithConfig(middleware.KeyAuthConfig{
		KeyLookup:  fmt.Sprintf("header:%s", echo.HeaderAuthorization),
		AuthScheme: "Bearer",
		Skipper:    Skipper,
		Validator:  TokenValidator,
	})
}

func Skipper(c echo.Context) bool {
	if os.Getenv("SKIP_AUTHN") != "" {
		return true
	}
	return false
}

func TokenValidator(token string, c echo.Context) (bool, error) {
	return true, nil
}
