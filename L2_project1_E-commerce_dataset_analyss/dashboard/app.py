import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7FAFC;
        color: #1F2937;
    }

    h1 {
        color: #0B5ED7;
    }

    h2, h3 {
        color: #0B5ED7;
    }

    .stMetric {
        background-color: #FFFFFF;
        border: 1px solid #D6E4F0;
        padding: 15px;
        border-radius: 10px;
    }

    [data-testid="stMetricLabel"] {
        color: #5B6B7A;
    }

    [data-testid="stMetricValue"] {
        color: #0B5ED7;
    }

    button[data-baseweb="tab"] {
        background-color: #FF0000 !important;
        color: #FFFFFF !important;
        border-radius: 6px 6px 0 0;
        margin-right: 4px;
    }

    button[data-baseweb="tab"]:hover {
        background-color: #FF0000 !important;
        color: #FFFFFF !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #0B5ED7 !important;
        color: #FFFFFF !important;
    }

    button[data-baseweb="tab"][aria-selected="true"]:hover {
        background-color: #0B5ED7 !important;
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("E-Commerce Analytics Dashboard")

st.write(
    "Interactive analysis of sales, revenue, products, "
    "countries, and monthly performance."
)

@st.cache_data
def load_data():
    return pd.read_csv("./data/Online Retail.csv", encoding="latin-1")

df = load_data()

df = df.drop_duplicates()
df = df.dropna(subset=["Description"])
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

merchandise_df = df[
    ~df["Description"].str.contains(
        "POSTAGE|Manual",
        case=False,
        na=False
    )
].copy()

st.sidebar.header("Dashboard Filters")

country_list = sorted(merchandise_df["Country"].unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All Countries"] + country_list
)

min_date = merchandise_df["InvoiceDate"].min().date()
max_date = merchandise_df["InvoiceDate"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

product_list = sorted(merchandise_df["Description"].unique())

selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All Products"] + product_list
)

filtered_df = merchandise_df.copy()

if selected_country != "All Countries":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if len(selected_dates) == 2:
    start_date = pd.Timestamp(selected_dates[0])
    end_date = pd.Timestamp(selected_dates[1]) + pd.Timedelta(days=1)

    filtered_df = filtered_df[
        (filtered_df["InvoiceDate"] >= start_date)
        &
        (filtered_df["InvoiceDate"] < end_date)
    ]

if selected_product != "All Products":
    filtered_df = filtered_df[
        filtered_df["Description"] == selected_product
    ]

if filtered_df.empty:
    st.warning(
        "No data is available for the selected filters."
    )
    st.stop()

total_revenue = filtered_df["Revenue"].sum()
total_orders = filtered_df["InvoiceNo"].nunique()
total_quantity = filtered_df["Quantity"].sum()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)

product_revenue = (
    filtered_df
    .groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_product = product_revenue.index[0]

country_revenue = (
    filtered_df
    .groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_country = country_revenue.index[0]

st.subheader("Sales KPI Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"{total_revenue:,.2f}"
)

col2.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col3.metric(
    "Total Quantity",
    f"{total_quantity:,}"
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Average Order Value",
    f"{average_order_value:,.2f}"
)

col5.metric(
    "Top Product",
    top_product
)

col6.metric(
    "Top Country",
    top_country
)

overview_tab, product_tab, country_tab = st.tabs(
    [
        "Overview",
        "Product Analysis",
        "Country Analysis"
    ]
)

with overview_tab:
    st.subheader("Monthly Revenue Trend")

    filtered_df["Month"] = (
        filtered_df["InvoiceDate"]
        .dt.to_period("M")
        .dt.to_timestamp()
    )

    monthly_revenue = (
        filtered_df
        .groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    fig_monthly = px.line(
        monthly_revenue,
        x="Month",
        y="Revenue",
        title="Monthly Revenue Trend",
        markers=True
    )

    fig_monthly.update_traces(
        line=dict(
            color="#0B5ED7",
            width=3
        ),
        marker=dict(
            size=7
        )
    )

    fig_monthly.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="Revenue",
        hovermode="x unified"
    )

    st.plotly_chart(
        fig_monthly,
        use_container_width=True
    )

    monthly_growth = (
        monthly_revenue
        .set_index("Month")["Revenue"]
        .pct_change()
        * 100
    )

    latest_growth = monthly_growth.iloc[-1]

    if pd.isna(latest_growth):
        growth_text = "Not available"
    else:
        growth_text = f"{latest_growth:.2f}%"

    st.subheader("Latest Monthly Growth")

    st.metric(
        "Month-to-Month Growth",
        growth_text
    )

    st.subheader("Filtered Data")

    st.dataframe(
        filtered_df[
            [
                "InvoiceNo",
                "StockCode",
                "Description",
                "Quantity",
                "InvoiceDate",
                "UnitPrice",
                "Country",
                "Revenue"
            ]
        ].head(100),
        use_container_width=True
    )

with product_tab:
    st.subheader(
        "Top 10 Merchandise Products by Revenue"
    )

    top_10_products = (
        product_revenue
        .head(10)
        .sort_values()
        .reset_index()
    )

    fig_products = px.bar(
        top_10_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 Products by Revenue"
    )

    fig_products.update_traces(
        marker_color="#0B5ED7"
    )

    fig_products.update_layout(
        template="plotly_white",
        xaxis_title="Revenue",
        yaxis_title="Product"
    )

    st.plotly_chart(
        fig_products,
        use_container_width=True
    )

    st.subheader(
        "Top 10 Products by Quantity Sold"
    )

    quantity_products = (
        filtered_df
        .groupby("Description")["Quantity"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .sort_values()
        .reset_index()
    )

    fig_quantity = px.bar(
        quantity_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top 10 Products by Quantity Sold"
    )

    fig_quantity.update_traces(
        marker_color="#2E86C1"
    )

    fig_quantity.update_layout(
        template="plotly_white",
        xaxis_title="Quantity Sold",
        yaxis_title="Product"
    )

    st.plotly_chart(
        fig_quantity,
        use_container_width=True
    )

    st.subheader(
        "Product Performance Table"
    )

    product_table = (
        filtered_df
        .groupby("Description")
        .agg(
            Quantity_Sold=("Quantity", "sum"),
            Revenue=("Revenue", "sum"),
            Orders=("InvoiceNo", "nunique")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .reset_index()
    )

    product_table["Revenue"] = (
        product_table["Revenue"]
        .round(2)
    )

    st.dataframe(
        product_table,
        use_container_width=True
    )

with country_tab:
    st.subheader(
        "Country Revenue Analysis"
    )

    top_10_countries = (
        country_revenue
        .head(10)
        .sort_values()
        .reset_index()
    )

    fig_countries = px.bar(
        top_10_countries,
        x="Revenue",
        y="Country",
        orientation="h",
        title="Top 10 Countries by Revenue"
    )

    fig_countries.update_traces(
        marker_color="#0B5ED7"
    )

    fig_countries.update_layout(
        template="plotly_white",
        xaxis_title="Revenue",
        yaxis_title="Country"
    )

    st.plotly_chart(
        fig_countries,
        use_container_width=True
    )

    st.subheader(
        "Country Performance Table"
    )

    country_table = (
        filtered_df
        .groupby("Country")
        .agg(
            Revenue=("Revenue", "sum"),
            Orders=("InvoiceNo", "nunique"),
            Quantity=("Quantity", "sum")
        )
        .sort_values(
            "Revenue",
            ascending=False
        )
        .reset_index()
    )

    country_table["Revenue"] = (
        country_table["Revenue"]
        .round(2)
    )

    st.dataframe(
        country_table,
        use_container_width=True
    )

    st.subheader(
        "Quantity Sold vs Revenue"
    )

    product_relationship = (
        filtered_df
        .groupby("Description")
        .agg(
            Quantity=("Quantity", "sum"),
            Revenue=("Revenue", "sum")
        )
        .reset_index()
    )

    fig_scatter = px.scatter(
        product_relationship,
        x="Quantity",
        y="Revenue",
        hover_name="Description",
        title="Product Quantity vs Revenue"
    )

    fig_scatter.update_traces(
        marker=dict(
            color="#0B5ED7",
            size=8
        )
    )

    fig_scatter.update_layout(
        template="plotly_white",
        xaxis_title="Quantity Sold",
        yaxis_title="Revenue"
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )