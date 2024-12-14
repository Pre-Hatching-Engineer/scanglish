package middleware

import (
	"os"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func AuthMiddleware() echo.MiddlewareFunc {
	return middleware.KeyAuthWithConfig(middleware.KeyAuthConfig{
		KeyLookup:  "header:Authorization",
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

}
