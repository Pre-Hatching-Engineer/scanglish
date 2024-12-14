package database

import (
	"fmt"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

type user struct {
	gorm.Model
	Username string
	Password string
}

func NewDatabase(username, password, host, database string) (*gorm.DB, error) {
	dsn := fmt.Sprintf("%s:%s&tcp(%s)/%s?charset=utf8mb4&parseTime=True", username, password, host, database)
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}
	return db, nil
}
