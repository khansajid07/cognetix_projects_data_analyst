# Bank Customer Churn Analysis

## Project Overview

This project analyzes customer churn in a banking dataset using Exploratory Data Analysis (EDA), statistical summaries, visualizations, and an interactive dashboard.

The main objective is to understand customer behavior, identify patterns between customers who stayed and customers who churned, and determine the factors that are most strongly associated with customer churn.

The project uses Python, Pandas, Matplotlib, Seaborn, Plotly, and Streamlit.

## Objectives

- Analyze customer churn and retention patterns
- Compare churned and retained customers
- Analyze Age, Balance, Tenure, and Credit Score
- Analyze churn by Geography and Gender
- Analyze the effect of active membership on churn
- Analyze churn based on the number of products
- Create a correlation heatmap
- Identify important factors associated with customer churn
- Build an interactive dashboard for customer churn analysis

## Dataset

**Dataset Source:**  
Kaggle: Churn for Bank Customers

**Dataset File Used in This Project:**

`churn.csv`

The dataset contains **10,000 bank customer records** and **14 original columns**.

### Main Columns

- `CustomerId`
- `Surname`
- `CreditScore`
- `Geography`
- `Gender`
- `Age`
- `Tenure`
- `Balance`
- `NumOfProducts`
- `HasCrCard`
- `IsActiveMember`
- `EstimatedSalary`
- `Exited`

An additional column called `Churn_Status` was created during the analysis.

## Technologies Used

- Python 3.9+
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## Project Structure

```text
Bank_Churn_Analysis/
│
├── data/
│   └── churn.csv
│
├── visuals/
│   ├── age_distribution.png
│   ├── age_churn_boxplot.png
│   ├── tenure_distribution.png
│   ├── tenure_churn_boxplot.png
│   ├── balance_distribution.png
│   ├── balance_churn_boxplot.png
│   ├── salary_distribution.png
│   ├── salary_churn_boxplot.png
│   ├── credit_score_distribution.png
│   ├── credit_score_churn_boxplot.png
│   ├── churn_vs_age.png
│   ├── churn_vs_credit_score.png
│   ├── churn_vs_balance.png
│   ├── churn_vs_tenure.png
│   ├── churn_by_gender.png
│   ├── churn_by_geography.png
│   ├── correlation_heatmap.png
│   ├── churn_by_active_membership.png
│   ├── churn_by_products.png
│   └── churn_overview.png
│
├── dashboard/
│   └── app.py
│
├── Bank_Churn_Analysis.ipynb
│
└── README.md
```

# Data Analysis

## Data Validation

The dataset was checked for:

- Dataset shape
- Column information
- Duplicate records
- Missing values
- Data types
- Statistical summary
- Categorical distributions

The dataset contains **10,000 records**.

There were:

- **0 duplicate rows**
- **0 missing values**

## Overall Churn

The dataset contains:

- **7,963 customers who stayed**
- **2,037 customers who churned**
- **Overall churn rate: 20.37%**

This means approximately **one out of every five customers** in the dataset has exited the bank.

# Key Findings

## Age

Age shows an important difference between churned and retained customers.

### Average Age

| Customer Status | Average Age |
|---|---:|
| Churned customers | 44.84 years |
| Stayed customers | 37.41 years |

Older customers in this dataset have a higher tendency to churn.

## Balance

Churned customers have a higher average balance than customers who stayed.

### Average Balance

| Customer Status | Average Balance |
|---|---:|
| Churned customers | 91,108.54 |
| Stayed customers | 72,745.30 |

Balance has a positive relationship with churn, although the relationship is relatively weak.

## Tenure

Tenure shows very little difference between churned and retained customers.

### Average Tenure

| Customer Status | Average Tenure |
|---|---:|
| Churned customers | 4.93 years |
| Stayed customers | 5.03 years |

This suggests that tenure is not a major churn factor in this dataset.

## Credit Score

The average credit score is slightly lower among churned customers.

### Average Credit Score

| Customer Status | Average Credit Score |
|---|---:|
| Churned customers | 645.35 |
| Stayed customers | 651.85 |

The distributions overlap considerably, so credit score appears to be a relatively weak churn factor.

## Estimated Salary

Estimated salary shows similar distributions for churned and retained customers.

### Average Salary

| Customer Status | Average Salary |
|---|---:|
| Churned customers | 101,465.68 |
| Stayed customers | 99,738.39 |

The difference is small, indicating that estimated salary is not a strong churn factor in this dataset.

## Gender

### Churn Rate by Gender

| Gender | Churn Rate |
|---|---:|
| Female | 25.07% |
| Male | 16.46% |

Female customers have a higher churn rate than male customers in this dataset.

## Geography

### Churn Rate by Country

| Geography | Churn Rate |
|---|---:|
| France | 16.15% |
| Germany | 32.44% |
| Spain | 16.67% |

Germany has the highest churn rate among the three countries.

The churn rate in Germany is approximately twice the churn rate observed in France and Spain.

## Active Membership

### Churn Rate by Membership Status

| Membership Status | Churn Rate |
|---|---:|
| Inactive members | 26.85% |
| Active members | 14.27% |

Inactive customers have a substantially higher churn rate.

This suggests that customer engagement and activity may be important factors associated with customer retention.

## Number of Products

Churn varies significantly according to the number of products held by customers.

| Number of Products | Customers | Churned | Churn Rate |
|---:|---:|---:|---:|
| 1 | 5,084 | 1,409 | 27.71% |
| 2 | 4,590 | 348 | 7.58% |
| 3 | 266 | 220 | 82.71% |
| 4 | 60 | 60 | 100.00% |

The 3-product and 4-product groups are relatively small, so their very high churn rates should be interpreted cautiously.

# Correlation Analysis

The correlation analysis shows the following relationships with `Exited`:

| Variable | Correlation with Churn |
|---|---:|
| Age | 0.29 |
| Balance | 0.12 |
| IsActiveMember | -0.16 |
| NumOfProducts | -0.05 |
| CreditScore | -0.03 |
| Tenure | -0.01 |
| HasCrCard | -0.01 |
| EstimatedSalary | 0.01 |

Age has the strongest positive numerical relationship with churn.

Active membership has a negative relationship with churn, meaning active customers are less likely to churn in this dataset.

Correlation values show relationships between variables but do not by themselves prove causation.

# Why Customers Churn

Based on the analysis, the main patterns associated with customer churn are:

- Older customers show higher churn rates.
- Customers with higher balances have a higher average churn level.
- Inactive members have a considerably higher churn rate than active members.
- Germany has a substantially higher churn rate than France and Spain.
- Female customers have a higher churn rate than male customers in this dataset.
- Customers with different numbers of products show large differences in churn rates.
- Credit score, tenure, and estimated salary show relatively weak relationships with churn.

# Interactive Dashboard

The project includes an interactive **Streamlit dashboard**.

The dashboard provides:

### Customer Filters

- Customer filters
- Geography filter
- Gender filter
- Membership status filter
- Number of products filter
- Customer age range filter

### KPIs

- Total customer KPI
- Churned customer KPI
- Churn rate KPI
- Average age KPI
- Average credit score KPI

### Visualizations

- Customer retention chart
- Churn rate by geography
- Churn rate by gender
- Churn rate by membership
- Age distribution
- Balance distribution
- Churn rate by number of products
- Churn rate by tenure
- Credit score analysis
- Correlation heatmap
- Filtered customer records

The dashboard is designed with a **dark navy and teal interface** to provide a different visual style from the previous project.

# Running the Jupyter Notebook

## Install the Required Libraries

```bash
pip install pandas matplotlib seaborn jupyter
```

## Start Jupyter Notebook

```bash
jupyter notebook
```

## Open the Notebook

```text
Bank_Churn_Analysis.ipynb
```

# Running the Dashboard

## Install Streamlit and Plotly

```bash
pip install streamlit plotly
```

## Navigate to the Dashboard Folder

```bash
cd dashboard
```

## Run the Application

```bash
streamlit run app.py
```

The dashboard will open in the browser.

# Business Insights

The analysis can help a bank focus customer retention efforts on groups showing higher churn patterns.

Potential areas for attention include:

- Older customers
- Inactive customers
- Customers in Germany
- Customers with higher balances
- Customer groups with unusually high churn based on product count

These findings can help support targeted customer retention strategies and further investigation into customer experience, engagement, and product usage.

# Conclusion

The **Bank Customer Churn Analysis** identifies several important patterns in customer churn.

Age, active membership, geography, balance, gender, and number of products show noticeable differences between churned and retained customers.

Among the numerical variables, **age has the strongest positive correlation with churn**, while **active membership has a negative relationship with churn**.

Tenure, estimated salary, and credit score show relatively weaker relationships with customer churn.

The interactive dashboard makes it easier to explore these patterns by applying filters and examining customer groups from different perspectives.

# Author

**Sajid Khan**

Data Analyst Intern
