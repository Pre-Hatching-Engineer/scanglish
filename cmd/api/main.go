package main

import (
	"os"
	"strings"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()
	e.HideBanner = true
	e.HidePort = true
	e.Use(middleware.Recover())
	e.Use(middleware.Secure())

	// cors
	origins := []string{"*"}
	if os.Getenv("ALLOW_ORIGINS") != "" {
		origins = strings.Split(os.Getenv("ALLOW_ORIGINS"), ",")
	}
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: origins,
	}))

}
