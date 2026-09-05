# E-Commerce Dataset Analysis

## Project Overview

This project focuses on analyzing an online retail e-commerce dataset to understand customer orders, revenue trends, product performance, and country-wise sales performance.

The analysis includes data cleaning, revenue calculation, best-selling product identification, country-wise revenue analysis, monthly revenue trends, sales KPIs, and an interactive Streamlit dashboard.

The project was completed as part of the Intermediate Stage Projects (Level-2).

## Objective

The main objectives of this project are:

- Analyze customer orders and sales performance
- Calculate revenue using Quantity × UnitPrice
- Identify best-selling products
- Analyze product-level performance
- Analyze country-wise revenue
- Identify monthly revenue trends
- Calculate important sales KPIs
- Create interactive and dashboard-ready visualizations
- Build an interactive Streamlit dashboard

## Dataset

**Dataset:** Online Retail Dataset

**Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/vijayuv/onlineretail

The dataset contains online retail transaction records with information about invoices, products, quantities, prices, customers, countries, and invoice dates.

## Dataset Columns

| Column | Description |
|---|---|
| InvoiceNo | Invoice number for the transaction |
| StockCode | Product stock code |
| Description | Product description |
| Quantity | Number of products purchased |
| InvoiceDate | Date and time of the transaction |
| UnitPrice | Price per product |
| CustomerID | Customer identification number |
| Country | Customer country |

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- GitHub

## Project Structure

```text
Ecommerce_Analysis/
│
├── data/
│   └── Online Retail.csv
│
|
├── analysis.ipynb
│
├── visuals/
│   ├── top_10_products.png
│   ├── top_10_countries.png
│   ├── monthly_revenue_trend.png
│   ├── top_10_merchandise_products.png
│   ├── product_revenue_heatmap.png
│   └── top_10_quantity_products.png
│
├── dashboard/
│   └── app.py
│
└── README.md
```

## 1. Import Libraries

The project uses Pandas for data loading, cleaning, grouping, and analysis.

Matplotlib and Seaborn are used for static visualizations.

Plotly is used to create interactive dashboard charts.

Streamlit is used to build the interactive dashboard.

## 2. Load Dataset

The `Online Retail.csv` file was loaded into a Pandas DataFrame.

The original dataset contained:

- 541,909 records
- 8 columns

## 3. Data Validation and Cleaning

The dataset was checked for duplicates, missing values, incorrect data types, negative quantities, and invalid prices.

### Duplicate Records

The dataset contained 5,268 duplicate rows.

Duplicate records were removed.

### Missing Values

The `Description` column contained 1,454 missing values.

Rows with missing product descriptions were removed.

The `CustomerID` column contained missing values, but it was not required for the main sales analysis.

### InvoiceDate

The `InvoiceDate` column was originally stored as an object.

It was converted to datetime format for time-based analysis.

### Quantity

The dataset contained negative quantity values.

Transactions with quantities less than or equal to zero were removed.

### UnitPrice

The dataset contained invalid non-positive unit prices.

Transactions with unit prices less than or equal to zero were removed.

### Cleaned Dataset

After cleaning, the dataset contained:

- 524,878 records
- 8 original columns

The minimum valid quantity was 1.

The minimum valid unit price was 0.001.

## 4. Revenue Calculation

Revenue was calculated for every transaction using:

```text
Revenue = Quantity × UnitPrice
```

A new `Revenue` column was created.

The total revenue in the cleaned dataset was approximately:

**10,642,110.80**

## 5. Best-Selling Products

Product performance was analyzed using both revenue and quantity sold.

The original dataset contains transaction descriptions such as postage and manual entries. These are not physical merchandise products.

Therefore, merchandise-only analysis excluded descriptions containing:

- POSTAGE
- Manual

This allowed the best-selling merchandise products to be analyzed separately.

## 6. Top Merchandise Products by Revenue

The top merchandise products by revenue were:

| Rank | Product | Revenue |
|---:|---|---:|
| 1 | REGENCY CAKESTAND 3 TIER | 174,156.54 |
| 2 | PAPER CRAFT , LITTLE BIRDIE | 168,469.60 |
| 3 | WHITE HANGING HEART T-LIGHT HOLDER | 106,236.72 |
| 4 | PARTY BUNTING | 99,445.23 |
| 5 | JUMBO BAG RED RETROSPOT | 94,159.81 |
| 6 | MEDIUM CERAMIC TOP STORAGE JAR | 81,700.92 |
| 7 | RABBIT NIGHT LIGHT | 66,870.03 |
| 8 | PAPER CHAIN KIT 50'S CHRISTMAS | 64,875.59 |
| 9 | ASSORTED COLOUR BIRD ORNAMENT | 58,927.62 |
| 10 | CHILLI LIGHTS | 54,096.36 |

The highest-revenue merchandise product was **REGENCY CAKESTAND 3 TIER**.

## 7. Top Products by Quantity Sold

The products with the highest quantities sold were:

| Rank | Product | Quantity Sold |
|---:|---|---:|
| 1 | PAPER CRAFT , LITTLE BIRDIE | 80,995 |
| 2 | MEDIUM CERAMIC TOP STORAGE JAR | 78,033 |
| 3 | WORLD WAR 2 GLIDERS ASSTD DESIGNS | 54,951 |
| 4 | JUMBO BAG RED RETROSPOT | 48,371 |
| 5 | WHITE HANGING HEART T-LIGHT HOLDER | 37,872 |
| 6 | POPCORN HOLDER | 36,749 |
| 7 | PACK OF 72 RETROSPOT CAKE CASES | 36,396 |
| 8 | ASSORTED COLOUR BIRD ORNAMENT | 36,362 |
| 9 | RABBIT NIGHT LIGHT | 30,739 |
| 10 | MINI PAINT SET VINTAGE | 26,633 |

The highest quantity sold was recorded for **PAPER CRAFT , LITTLE BIRDIE**.

## 8. Country-wise Revenue Analysis

Country performance was analyzed by grouping transaction revenue by country.

The top countries by revenue were:

| Rank | Country | Revenue |
|---:|---|---:|
| 1 | United Kingdom | 9,001,744.09 |
| 2 | Netherlands | 285,446.34 |
| 3 | EIRE | 283,140.52 |
| 4 | Germany | 228,678.40 |
| 5 | France | 209,625.37 |
| 6 | Australia | 138,453.81 |
| 7 | Spain | 61,558.56 |
| 8 | Switzerland | 57,067.60 |
| 9 | Belgium | 41,196.34 |
| 10 | Sweden | 38,367.83 |

The **United Kingdom** generated the highest revenue by a large margin.

## 9. Monthly Revenue Trend

Monthly revenue was calculated by extracting the month from `InvoiceDate` and grouping transactions by month.

| Month | Revenue |
|---|---:|
| December 2010 | 821,452.73 |
| January 2011 | 689,811.61 |
| February 2011 | 522,545.56 |
| March 2011 | 716,215.26 |
| April 2011 | 536,968.49 |
| May 2011 | 769,296.61 |
| June 2011 | 760,547.01 |
| July 2011 | 718,076.12 |
| August 2011 | 757,841.38 |
| September 2011 | 1,056,435.19 |
| October 2011 | 1,151,263.73 |
| November 2011 | 1,503,866.78 |
| December 2011 | 637,790.33 |

November 2011 recorded the highest monthly revenue at approximately **1.50 million**.

December 2011 shows lower revenue, but the dataset ends on December 9, 2011, so December 2011 is only a partial month and should not be directly compared with complete months.

## 10. Monthly Growth Trend

Month-to-month revenue growth was calculated using percentage change.

| Month | Growth |
|---|---:|
| January 2011 | -16.03% |
| February 2011 | -24.25% |
| March 2011 | +37.06% |
| April 2011 | -25.03% |
| May 2011 | +43.27% |
| June 2011 | -1.14% |
| July 2011 | -5.58% |
| August 2011 | +5.54% |
| September 2011 | +39.40% |
| October 2011 | +8.98% |
| November 2011 | +30.63% |
| December 2011 | -57.59% |

May 2011 recorded the highest positive month-to-month growth at approximately **43.27%**.

November 2011 also showed strong growth of approximately **30.63%**.

The December 2011 decline of **57.59%** should be interpreted carefully because the available data for December ends on December 9.

## 11. KPI Summary

The project calculated the following key performance indicators:

| KPI | Value |
|---|---:|
| Total Revenue | 10,642,110.80 |
| Total Orders | 19,960 |
| Total Merchandise Quantity | 5,561,579 |
| Unique Merchandise Products | 4,023 |
| Unique Countries | 38 |
| Top Merchandise Product | REGENCY CAKESTAND 3 TIER |
| Top Country | United Kingdom |

## 12. Visualizations

The project includes the following visualizations.

### Top 10 Products

A bar chart showing the highest-revenue merchandise products.

**File:**

`visuals/top_10_merchandise_products.png`

### Top 10 Countries

A bar chart comparing revenue across the top countries.

**File:**

`visuals/top_10_countries.png`

### Monthly Revenue Trend

A line chart showing how revenue changed over time.

**File:**

`visuals/monthly_revenue_trend.png`

### Product Revenue Heatmap

A heatmap was created to provide a visual comparison of product-level revenue performance.

**File:**

`visuals/product_revenue_heatmap.png`

### Top 10 Products by Quantity

A bar chart showing products with the highest quantities sold.

**File:**

`visuals/top_10_quantity_products.png`

## 13. Interactive Streamlit Dashboard

An interactive dashboard was created using Streamlit and Plotly.

The dashboard provides:

- Country selection
- All Countries option
- Product selection
- All Products option
- Date range filtering
- Total Revenue KPI
- Total Orders KPI
- Total Quantity KPI
- Average Order Value
- Top Product
- Top Country
- Interactive monthly revenue chart
- Interactive product revenue chart
- Interactive quantity chart
- Interactive country revenue chart
- Product performance table
- Country performance table
- Quantity versus revenue scatter plot

The dashboard is divided into three sections:

### Overview

Provides:

- Monthly Revenue Trend
- Month-to-Month Growth
- Filtered Transaction Data

### Product Analysis

Provides:

- Top 10 Products by Revenue
- Top 10 Products by Quantity Sold
- Product Performance Table

### Country Analysis

Provides:

- Top 10 Countries by Revenue
- Country Performance Table
- Quantity Sold versus Revenue analysis

## 14. Running the Dashboard

Install the required packages:

```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install plotly
pip install streamlit
pip install jupyter
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

Open the project directory and run:

```bash
streamlit run dashboard/app.py
```

The Streamlit dashboard will open in the browser.

## 15. Key Insights

1. The United Kingdom generated the highest revenue among all countries in the dataset.
2. REGENCY CAKESTAND 3 TIER was the highest-revenue merchandise product.
3. PAPER CRAFT , LITTLE BIRDIE had the highest quantity sold.
4. November 2011 recorded the highest monthly revenue.
5. Revenue increased strongly during September, October, and November 2011.
6. May 2011 recorded the highest positive month-to-month growth at approximately 43.27%.
7. The dataset contains 4,023 unique merchandise products after excluding postage and manual transaction descriptions.
8. The dataset covers 38 countries.
9. December 2011 shows a large decline compared with November, but December is only a partial month because the available data ends on December 9, 2011.
10. Product-level and country-level analysis provide useful information for understanding sales performance and revenue concentration.

## 16. What I Learned

Through this project, I learned how to:

- Load and inspect a large retail dataset using Pandas
- Identify and remove duplicate records
- Handle missing values
- Convert date columns into datetime format
- Remove invalid transaction records
- Create calculated columns
- Calculate revenue from quantity and unit price
- Group data by products and countries
- Analyze monthly sales trends
- Calculate month-to-month growth
- Identify top-performing products
- Create KPI summaries
- Build static visualizations using Matplotlib and Seaborn
- Create interactive visualizations using Plotly
- Build an interactive dashboard using Streamlit
- Add filters to a data analytics dashboard
- Present business insights from transaction data

## 17. Future Improvements

Possible improvements for this project include:

- Customer segmentation analysis
- Repeat customer analysis
- Average order value by country
- Product return and cancellation analysis
- Customer purchase frequency analysis
- RFM analysis
- Sales forecasting
- Customer-level dashboard filters
- Product search instead of a large product selector
- Additional interactive charts
- Deployment of the Streamlit dashboard online

## 18. Conclusion

This project provided a complete analysis of an online retail dataset, starting from data cleaning and validation and continuing through revenue calculation, product analysis, country analysis, KPI reporting, visualization, and interactive dashboard development.

The analysis identified the strongest products, countries, and revenue periods while also highlighting important considerations such as non-merchandise transactions and the partial December 2011 data.

The final Streamlit dashboard makes the analysis interactive by allowing users to filter the results by country, product, and date range and explore the resulting sales performance dynamically.

Overall, this project demonstrates practical skills in data cleaning, exploratory data analysis, revenue analysis, business intelligence, data visualization, KPI development, and interactive dashboard creation using Python.
