package main

import (
	"log"
	"mocorona-api/database"
	"mocorona-api/routers"
)

func main() {
	database.Setup()
	router := routers.Setup()
	if err := router.Run("localhost:8000"); err != nil {
		log.Fatal(err)
	}
}
