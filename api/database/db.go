package database

import (
	"fmt"
	"log"
	"os"

	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"

	"mocorona-api/models"
)

var DB *gorm.DB

func Setup() {
	host := os.Getenv("DB_HOST")
	port := os.Getenv("DB_PORT")
	dbname := os.Getenv("DB_NAME")
	user := os.Getenv("DB_USER")
	password := os.Getenv("DB_PASSWORD")

	db, err := gorm.Open("postgres", fmt.Sprintf("host=%s "+
		"port=%s dbname=%s user=%s password=%s sslmode=disable",
		host, port, dbname, user, password))

	if err != nil {
		log.Fatal(err)
	}

	db.LogMode(false)
	db.AutoMigrate([]models.CovidSummary{}, []models.VaccineSummary{})
	DB = db
}

func GetDB() *gorm.DB {
	return DB
}

func GetCovidSummaries(db *gorm.DB) ([]models.CovidSummary, error) {
	summaries := []models.CovidSummary{}
	query := db.Select("covid_summaries.*").Group("covid_summaries.id")

	if err := query.Find(&summaries).Error; err != nil {
		return summaries, err
	}
	return summaries, nil
}

func CreateCovidSummary(
	db *gorm.DB, summary models.CovidSummary) (models.CovidSummary, error) {

	if err := db.Create(&summary).Error; err != nil {
		return summary, err
	}
	return summary, nil
}

func GetVaccineSummaries(db *gorm.DB) ([]models.VaccineSummary, error) {
	summaries := []models.VaccineSummary{}
	query := db.Select("vaccine_summaries.*").Group("vaccine_summaries.id")

	if err := query.Find(&summaries).Error; err != nil {
		return summaries, err
	}
	return summaries, nil
}

func CreateVaccineSummary(
	db *gorm.DB, summary models.VaccineSummary) (models.VaccineSummary, error) {

	if err := db.Create(&summary).Error; err != nil {
		return summary, err
	}
	return summary, nil
}
