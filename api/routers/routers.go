package routers

import (
	"mocorona-api/database"
	"mocorona-api/handlers"

	"github.com/gin-gonic/gin"
)

func Setup() *gin.Engine {
	router := gin.Default()
	api := &handlers.APIEnv{
		DB: database.GetDB(),
	}

	router.GET("/covid-summaries", api.GetCovidSummaries)
	router.POST("/covid-summaries", api.CreateCovidSummary)

	return router
}
