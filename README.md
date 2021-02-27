# SQLAlchemy Homework - Surfs Up!

### Introduction

I'm taking a long vacation in Honolulu, Hawaii! For some reason, I feel like I need to do some climate analysis on the area in order to plan my trip!? At any rate, this is what I did.

## Step 1 - Climate Analysis and Exploration

I used Python and SQLAlchemy to do basic climate analysis and data exploration of my climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data, plotted the data, and printed summary statistics.

### Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations and determined the most active station.

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS) and plotted the results of the station with the highest number of observations as a histogram.

## Step 2 - Climate App

After completing the initial analysis, I designed a Flask API based on the queries I had developed with the following routes:

* Home page listing all routes that are available.

* `/api/v1.0/precipitation`

* `/api/v1.0/stations`

* `/api/v1.0/tobs`

* `/api/v1.0/<start>`

* `/api/v1.0/<start>/<end>`