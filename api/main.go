package main

import (
	"log"
	"mocorona-api/database"
	"mocorona-api/routers"

	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()
	database.Setup()
	router := routers.Setup()
	if err := router.Run("0.0.0.0:8001"); err != nil {
		log.Fatal(err)
	}
}
