package models

import (
	"time"

	"github.com/jinzhu/gorm"
)

type CovidSummary struct {
	gorm.Model
	Notification int
	Negative     int
	Confirmed    int
	Recovered    int
	Dead         int
	Release      time.Time
}

type VaccineSummary struct {
	gorm.Model
	UniqueDose  int
	FirstDose   int
	SecondDose  int
	BoosterDose int
	Target      string
	Release     time.Time
}
