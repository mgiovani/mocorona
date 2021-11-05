package handlers

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/gorm"

	"mocorona-api/database"
	"mocorona-api/models"
)

type APIEnv struct {
	DB *gorm.DB
}

func (api *APIEnv) GetCovidSummaries(c *gin.Context) {
	summaries, err := database.GetCovidSummaries(api.DB)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, summaries)
}

func (api *APIEnv) CreateCovidSummary(c *gin.Context) {
	summary := models.CovidSummary{}
	err := c.BindJSON(&summary)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}

	summary, err = database.CreateCovidSummary(api.DB, summary)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusCreated, summary)
}

func (api *APIEnv) GetVaccineSummaries(c *gin.Context) {
	summaries, err := database.GetVaccineSummaries(api.DB)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusOK, summaries)
}

func (api *APIEnv) CreateVaccineSummary(c *gin.Context) {
	summary := models.VaccineSummary{}
	err := c.BindJSON(&summary)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}

	summary, err = database.CreateVaccineSummary(api.DB, summary)
	if err != nil {
		log.Print(err)
		c.JSON(http.StatusInternalServerError, err.Error())
		return
	}
	c.JSON(http.StatusCreated, summary)
}
