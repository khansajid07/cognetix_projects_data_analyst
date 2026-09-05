# Project 3 - COVID-19 Data Analysis

## Project Overview

This project focuses on analyzing COVID-19 data to understand daily case trends, case progression, and country-level differences.

The analysis covers confirmed cases, active cases, recovered cases, deaths, daily new cases, and 7-day rolling averages. The project also compares COVID-19 trends across India, China, and the US.

An interactive Streamlit dashboard was also created to allow users to select a country and explore its COVID-19 statistics and trends.

This project was completed as part of my Data Analyst Internship.

## Objectives

The main objectives of this project are:

* Load and understand the COVID-19 dataset
* Validate and clean the dataset
* Convert the Date column into datetime format
* Filter the dataset by country
* Analyze daily COVID-19 cases
* Calculate a 7-day rolling average
* Analyze confirmed, active, recovered, and death cases
* Compare COVID-19 trends across India, China, and the US
* Create visualizations to understand case progression
* Build an interactive Streamlit dashboard
* Extract key insights from the analysis

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

## Dataset

The dataset used for this project is the COVID-19 Data Report dataset from Kaggle.

Dataset source:

https://www.kaggle.com/datasets/imdevskp/corona-virus-report

The project uses the `full_grouped.csv` dataset for the main analysis.

The dataset contains information about:

* Date
* Country/Region
* Confirmed Cases
* Deaths
* Recovered Cases
* Active Cases
* New Cases
* New Deaths
* New Recovered
* WHO Region

The dataset contains 35,156 records.

## Project Structure

```text
Project-3-COVID-19-Data-Analysis/
│
├── analysis.ipynb
├── README.md
│
├── data/
│   └── full_grouped.csv
│
├── dashboard/
│   └── app.py
│
└── visuals/
    ├── daily_cases.png
    ├── rolling_average.png
    ├── confirmed_cases.png
    ├── active_cases.png
    ├── recovered_cases.png
    ├── deaths.png
    ├── country_comparison.png
    ├── confirmed_comparison.png
    └── deaths_comparison.png
