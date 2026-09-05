# Project 3 - COVID-19 Data Analysis

## Project Overview

This project focuses on analyzing COVID-19 data to understand daily case trends, case progression, and country-level differences.

The analysis covers confirmed cases, active cases, recovered cases, deaths, daily new cases, and 7-day rolling averages. The project also compares COVID-19 trends across India, China, and the US.

An interactive Streamlit dashboard was also created to allow users to select a country and explore its COVID-19 statistics and trends.

This project was completed as part of my Data Analyst Internship.

## Objectives

The main objectives of this project are:

- Load and understand the COVID-19 dataset
- Validate and clean the dataset
- Convert the Date column into datetime format
- Filter the dataset by country
- Analyze daily COVID-19 cases
- Calculate a 7-day rolling average
- Analyze confirmed, active, recovered, and death cases
- Compare COVID-19 trends across India, China, and the US
- Create visualizations to understand case progression
- Build an interactive Streamlit dashboard
- Extract key insights from the analysis

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## Dataset

The dataset used for this project is the COVID-19 Data Report dataset from Kaggle.

Dataset source:

https://www.kaggle.com/datasets/imdevskp/corona-virus-report

The project uses the `full_grouped.csv` dataset for the main analysis.

The dataset contains information about:

- Date
- Country/Region
- Confirmed Cases
- Deaths
- Recovered Cases
- Active Cases
- New Cases
- New Deaths
- New Recovered
- WHO Region

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
```

## Data Validation and Cleaning

The dataset was checked to understand its structure and data quality.

The following steps were performed:

- Loaded the dataset using Pandas
- Checked the first few records
- Checked the number of rows and columns
- Checked column names
- Checked data types
- Checked missing values
- Checked duplicate records
- Converted the `Date` column into datetime format
- Filtered country-level data
- Sorted the data by date

The `full_grouped.csv` dataset was used as the main dataset for the analysis.

## Analysis Performed

### 1. India Country Analysis

India was selected for detailed country-level analysis.

The data was filtered using the `Country/Region` column and sorted according to date.

The following COVID-19 measures were analyzed:

- Confirmed cases
- Deaths
- Recovered cases
- Active cases
- New cases
- New deaths
- New recovered

### 2. Daily COVID-19 Cases

Daily COVID-19 cases in India were analyzed using the existing `New cases` column.

The daily case trend was visualized to understand how newly reported cases changed over time.

The `New cases` column represents newly reported cases, while `Confirmed` represents the cumulative number of confirmed cases.

### 3. 7-Day Rolling Average

A 7-day rolling average was calculated to smooth daily fluctuations in new COVID-19 cases.

The calculation was performed using:

```python
india["rolling_cases"] = (
    india["New cases"].rolling(7).mean()
)
```

The rolling average provides a smoother view of the overall daily case trend.

### 4. Confirmed Cases in India

The cumulative confirmed cases in India were analyzed over time.

The analysis shows a strong increase in confirmed cases during the later part of the available dataset.

India recorded 1,480,073 confirmed cases by 27 July 2020.

### 5. Active Cases in India

Active COVID-19 cases were analyzed to understand the number of ongoing active cases over time.

India recorded its highest active case count of 495,499 on 27 July 2020.

### 6. Recovered Cases in India

Recovered cases were analyzed to understand how the number of recovered patients changed over time.

India recorded its highest number of newly reported recoveries at 36,141 on 25 July 2020.

### 7. Deaths in India

COVID-19 deaths were analyzed using the `Deaths` and `New deaths` columns.

The highest number of newly reported deaths in India was 2,003 on 16 June 2020.

### 8. Country Comparison

COVID-19 confirmed cases were compared across:

- India
- China
- US

A time-series chart was created to compare the progression of confirmed cases across these three countries.

The analysis shows that the three countries had different COVID-19 case progression patterns during the available period.

### 9. Final Country Comparison

The latest available records for India, China, and the US were used to compare:

- Confirmed cases
- Deaths
- Recovered cases
- Active cases

The US had the highest confirmed case count among India, China, and the US at the end of the dataset.

## Visualizations

The following visualizations were created as part of the analysis:

- Daily COVID-19 Cases in India
- Daily Cases with 7-Day Rolling Average
- Confirmed Cases in India
- Active Cases in India
- Recovered Cases in India
- Deaths in India
- India vs China vs US Confirmed Cases
- Final Confirmed Cases Comparison
- Final Deaths Comparison

The chart images are available in the `visuals` folder.

## Streamlit Dashboard

An interactive Streamlit dashboard was created as an additional part of the project.

The dashboard allows users to select a country and view its COVID-19 statistics.

The dashboard includes:

- Country selection
- Latest confirmed cases
- Latest deaths
- Latest recovered cases
- Latest active cases
- Confirmed cases trend
- Active cases trend
- Recovered cases trend
- Deaths trend
- Daily new cases
- 7-day rolling average

The dashboard provides an interactive way to explore COVID-19 data at the country level.

## Dashboard Features

### Country Selection

Users can select a country from the dropdown menu.

The dashboard then displays the latest available COVID-19 statistics for the selected country.

### Latest Reported Data

The dashboard displays four key metrics:

- Confirmed
- Deaths
- Recovered
- Active

### COVID-19 Trend Charts

The dashboard provides trend charts for:

- Confirmed Cases
- Active Cases
- Recovered Cases
- Deaths
- Daily New Cases
- 7-Day Rolling Average

## How to Run the Dashboard

Install Streamlit using:

```bash
pip install streamlit
```

Run the dashboard from the project folder:

```bash
streamlit run dashboard/app.py
```

The dashboard will open in a web browser.

## Key Insights

1. India recorded 1,480,073 confirmed cases by 27 July 2020 in the dataset.
2. India's highest active case count was 495,499 on 27 July 2020.
3. India's highest number of new cases was 49,981 on 26 July 2020.
4. India's highest number of newly reported recoveries was 36,141 on 25 July 2020.
5. India's highest number of newly reported deaths was 2,003 on 16 June 2020.
6. The 7-day rolling average provides a smoother view of daily COVID-19 case trends.
7. Confirmed cases in India increased substantially during the later part of the available dataset.
8. The US had the highest confirmed case count among India, China, and the US at the end of the dataset.
9. China showed an earlier increase in confirmed cases, while India showed a stronger increase later in the available period.
10. India, China, and the US showed different COVID-19 case progression patterns.

## What I Learned

Through this project, I practiced:

- Loading and working with CSV data using Pandas
- Inspecting and validating a dataset
- Converting columns to appropriate data types
- Filtering data by country
- Sorting data by date
- Working with cumulative and daily case data
- Creating rolling averages
- Using Pandas for data analysis
- Creating line charts using Matplotlib
- Creating country comparisons
- Creating charts for data interpretation
- Building an interactive dashboard using Streamlit
- Presenting data-driven insights

## Future Improvements

Some possible improvements for this project are:

- Add more countries to the comparison
- Add interactive Plotly visualizations
- Add interactive date-range filters
- Add regional comparisons
- Add percentage growth calculations
- Add additional dashboard metrics
- Add more detailed statistical analysis
- Deploy the Streamlit dashboard online
- Add more interactive charts and tables

## Conclusion

This project provided practical experience in analyzing real-world COVID-19 data using Python.

The analysis helped identify daily case trends, confirmed cases, active cases, recoveries, and deaths. It also provided a comparison of COVID-19 case progression across India, China, and the US.

The 7-day rolling average helped provide a smoother view of daily case fluctuations, while the country comparison helped identify differences in case progression.

The Streamlit dashboard further improved the project by providing an interactive way to explore COVID-19 statistics for different countries.

Overall, this project provided practical experience in data cleaning, data analysis, visualization, country-level comparison, and dashboard development using Python.
