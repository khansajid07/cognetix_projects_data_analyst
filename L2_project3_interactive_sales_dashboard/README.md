# Interactive Sales Dashboard - Power BI

## Project Overview

This project is an interactive Sales Dashboard built using Power BI. The dashboard provides a clear view of sales, profit, orders, delivery performance, product performance, customer segments, categories, regions, and states.

The dashboard is designed to allow users to interact with the data using filters, drill-downs, and interactive visualizations.

## Objective

The main objective of this project is to build an interactive, filter-enabled sales dashboard that helps users:

- Monitor key sales and profit KPIs
- Analyze sales trends over time
- Compare regional performance
- Analyze category and sub-category performance
- Understand customer segment performance
- Identify top-performing products
- Analyze state-level sales
- Explore the data using interactive filters

## Dataset

The project uses the Superstore dataset containing order, customer, product, sales, and profit information.

The dataset includes fields such as:

- Order ID
- Order Date
- Ship Date
- Ship Mode
- Customer ID
- Customer Name
- Segment
- Country
- City
- State
- Postal Code
- Region
- Product ID
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

## Tools and Technologies

- Power BI Desktop
- Power Query
- DAX
- Microsoft Excel
- Data Visualization
- Data Cleaning and Transformation

## Data Preparation

The dataset was imported into Power BI and prepared using Power Query.

The data preparation process included:

- Checking column names and data types
- Checking missing values and errors
- Verifying date columns
- Verifying numerical columns
- Creating a Delivery Days column
- Converting delivery duration into numerical day values
- Preparing the dataset for analysis

No duplicate Order IDs were removed because a single order can contain multiple product records.

## DAX Measures

The following measures were created for the dashboard:

    Total Sales = SUM(Orders[Sales])

    Total Profit = SUM(Orders[Profit])

    Total Orders = DISTINCTCOUNT(Orders[Order ID])

    Average Delivery Days = AVERAGEX(Orders, DATEDIFF(Orders[Order Date], Orders[Ship Date], DAY))

## Key Performance Indicators

The dashboard contains four main KPI cards:

- Total Sales: 2.30M
- Total Profit: 286.40K
- Total Orders: 5K
- Average Delivery Days: 3.96

These values represent the overall dataset when no filters are applied.

## Dashboard Features

### Interactive Filters

Users can filter the dashboard by:

- Region
- Category
- Segment
- Order Date

The filters update the dashboard visuals dynamically.

### Sales Trend

The Sales Trend by Year visual shows how sales change over time.

### Category Analysis

The dashboard includes category-level sales analysis with drill-down functionality from Category to Sub-Category.

### Regional Profit Analysis

Profit by Region helps compare profitability across different regions.

### Customer Segment Analysis

Sales and Profit by Segment provides a comparison of customer segments.

### Category Sales Distribution

The Sales Distribution by Category chart shows the contribution of each category to overall sales.

### Top 10 Products

The Top 10 Products by Sales visual identifies the highest-selling products.

### State-Level Sales Map

The Sales by State map provides a geographical view of sales performance across states.

### Reset Filters

A Reset Filters button allows users to return the dashboard to its default state.

## Dashboard Visualizations

The dashboard includes:

- KPI Cards
- Line Chart
- Bar Charts
- Pie Chart
- Filled Map
- Interactive Slicers
- Drill-Down Visual
- Reset Filters Button
- Custom Tooltip

## Dashboard Preview

![Interactive Sales Dashboard](screenshots/dashboard.png)

## Key Insights

The dashboard allows users to identify:

- Overall sales and profitability
- Sales trends over time
- Regional differences in profit
- Category and sub-category performance
- Customer segment performance
- Top-performing products
- State-level sales distribution
- Delivery performance

## Skills Demonstrated

This project demonstrates practical skills in:

- Power BI
- Power Query
- DAX
- Data Cleaning
- Data Transformation
- Data Visualization
- Dashboard Design
- KPI Development
- Interactive Reporting
- Drill-Down Analysis
- Geographical Data Visualization
- Business Intelligence

## Project Outcome

The final dashboard provides an interactive business intelligence solution for analyzing sales performance and identifying important business trends.

The project demonstrates how raw sales data can be transformed into an interactive and professional Power BI dashboard for business analysis.
