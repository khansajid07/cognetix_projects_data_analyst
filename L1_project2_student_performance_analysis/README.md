# Project 2 - Student Performance Analysis

## Project Overview

This project focuses on analyzing student academic performance using the Student Performance in Exams dataset.

The analysis covers mathematics, reading, and writing scores. The main purpose is to calculate average scores, identify top-performing students, compare performance across different groups, and extract useful insights from the data.

This project was completed as part of my Data Analyst Internship.

## Objectives

The main objectives of this project are:

* Load and understand the student performance dataset
* Validate the dataset and check for missing or invalid values
* Calculate average scores for Mathematics, Reading, and Writing
* Create a total score for each student
* Identify the top-performing students
* Analyze performance by gender
* Analyze performance based on parental education level
* Compare performance across race/ethnicity groups
* Create visualizations to understand the data
* Extract key insights from the analysis

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## Dataset

The dataset used for this project is the Student Performance in Exams dataset from Kaggle.

Dataset source:

https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

The dataset contains 1,000 student records and includes information about:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch
* Test Preparation Course
* Math Score
* Reading Score
* Writing Score

## Project Structure

```text
Project-2-Student-Performance-Analysis/
│
├── analysis.ipynb
├── StudentsPerformance.csv
├── README.md
│
└── visuals/
    ├── math_distribution.png
    ├── gender_average.png
    ├── parental_education.png
    └── race_performance.png
```

## Data Validation

The dataset was checked for missing values, negative scores, and data types.

The dataset contains 1,000 records and no missing values were detected during the analysis.

## Analysis Performed

### 1. Subject Average Scores

The average scores calculated from the dataset are:

| Subject | Average Score |
| ------- | ------------: |
| Math    |         66.09 |
| Reading |         69.17 |
| Writing |         68.05 |

Reading has the highest average score, while Mathematics has the lowest average score among the three subjects.

### 2. Top Performing Students

A `total_score` column was created by adding the Mathematics, Reading, and Writing scores.

The students were then sorted by their total score to identify the top-performing students.

The highest-performing students achieved very high scores, including students with a total score of 300 out of 300.

### 3. Gender Analysis

Average scores were compared between male and female students.

The analysis shows that male students have a higher average Mathematics score, while female students have higher average Reading and Writing scores.

### 4. Parental Education Analysis

Student performance was compared across different parental education levels.

The results show that students whose parents have higher levels of education generally have higher average scores.

### 5. Race/Ethnicity Analysis

Average Mathematics, Reading, and Writing scores were compared across race/ethnicity groups.

Group E has the highest average performance across the three subjects.

## Visualizations

The following visualizations were created as part of the analysis:

* Distribution of Math Scores
* Average Scores by Gender
* Parental Education vs Student Performance
* Race/Ethnicity vs Average Scores

The chart images are available in the `visuals` folder.

## Key Insights

1. Reading has the highest overall average score at 69.17, followed by Writing at 68.05 and Mathematics at 66.09.

2. Male students have a higher average Mathematics score than female students.

3. Female students perform better in Reading and Writing compared with male students.

4. Students whose parents have higher levels of education generally show stronger academic performance.

5. Students with parents holding a master's degree have the highest average scores across the three subjects.

6. Group E has the highest average Mathematics score at 73.82 and shows the strongest overall performance among the race/ethnicity groups.

7. The highest-performing students achieved exceptional results, including three students with a perfect total score of 300 out of 300.

8. Group E is strongly represented among the highest-performing students.

9. Reading and Writing scores are higher than Mathematics scores on average.

10. The dataset contains 1,000 student records with no missing values detected.

## What I Learned

Through this project, I practiced:

* Loading and working with CSV data using Pandas
* Inspecting and validating a dataset
* Calculating averages
* Creating new columns
* Sorting and ranking records
* Using `groupby()` for analysis
* Creating visualizations using Matplotlib and Seaborn
* Interpreting data and identifying patterns
* Writing data-driven insights

## Future Improvements

Some possible improvements for this project are:

* Analyze the impact of the test preparation course
* Perform correlation analysis between subjects
* Explore relationships between different variables
* Create an interactive dashboard using Power BI or Tableau
* Perform more detailed statistical analysis
* Build a model to predict student performance

## Conclusion

This project provided practical experience in performing basic data analysis using Python. The analysis helped identify differences in student performance across subjects, gender, parental education levels, and race/ethnicity groups.

The project also provided experience in data validation, statistical calculations, visualization, and communicating findings from a dataset.

