package handler

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func Login(c echo.Context) error {
	username := c.FormValue("username")
	password := c.FormValue("password")

	// usernameとpasswordの認証

	return c.JSON(http.StatusUnauthorized, echo.Map{"message": "Invalid username or password"})
}
