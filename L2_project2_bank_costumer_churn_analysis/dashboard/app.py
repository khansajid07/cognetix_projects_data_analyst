import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Customer Churn Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background-color: #0B1220;
    color: #E5E7EB;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: #E5E7EB;
}

h1 {
    color: #F8FAFC;
    font-size: 36px;
}

h2, h3 {
    color: #F8FAFC;
}

p {
    color: #CBD5E1;
}

[data-testid="stMetric"] {
    background-color: #151F32;
    border: 1px solid #24324A;
    border-radius: 14px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8;
}

[data-testid="stMetricValue"] {
    color: #F8FAFC;
}

div[data-baseweb="select"] > div {
    background-color: #1E293B;
    border-color: #334155;
}

.stButton > button {
    background-color: #14B8A6;
    color: white;
    border: none;
    border-radius: 8px;
}

.stButton > button:hover {
    background-color: #0D9488;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.dashboard-card {
    background-color: #151F32;
    border: 1px solid #24324A;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 15px;
}

.section-title {
    color: #5EEAD4;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}

.small-text {
    color: #94A3B8;
    font-size: 14px;
}

hr {
    border-color: #24324A;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("./data/churn.csv")

df["Churn_Status"] = df["Exited"].map({
    0: "Stayed",
    1: "Churned"
})

st.sidebar.markdown("## Customer Filters")
st.sidebar.markdown("Use the filters below to explore churn patterns.")

country_options = sorted(df["Geography"].unique())
gender_options = sorted(df["Gender"].unique())
active_options = ["All", "Active", "Inactive"]
product_options = sorted(df["NumOfProducts"].unique())

country_filter = st.sidebar.selectbox(
    "Geography",
    ["All Countries"] + country_options
)

gender_filter = st.sidebar.selectbox(
    "Gender",
    ["All Genders"] + gender_options
)

active_filter = st.sidebar.selectbox(
    "Membership Status",
    active_options
)

product_filter = st.sidebar.multiselect(
    "Number of Products",
    product_options,
    default=product_options
)

age_range = st.sidebar.slider(
    "Customer Age",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (
        int(df["Age"].min()),
        int(df["Age"].max())
    )
)

filtered_df = df.copy()

if country_filter != "All Countries":
    filtered_df = filtered_df[
        filtered_df["Geography"] == country_filter
    ]

if gender_filter != "All Genders":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender_filter
    ]

if active_filter == "Active":
    filtered_df = filtered_df[
        filtered_df["IsActiveMember"] == 1
    ]

if active_filter == "Inactive":
    filtered_df = filtered_df[
        filtered_df["IsActiveMember"] == 0
    ]

filtered_df = filtered_df[
    filtered_df["NumOfProducts"].isin(product_filter)
]

filtered_df = filtered_df[
    filtered_df["Age"].between(
        age_range[0],
        age_range[1]
    )
]

total_customers = len(filtered_df)
churned_customers = int(filtered_df["Exited"].sum())

if total_customers > 0:
    churn_rate = (
        churned_customers /
        total_customers *
        100
    )

    average_age = filtered_df["Age"].mean()
    average_balance = filtered_df["Balance"].mean()
    average_credit_score = filtered_df["CreditScore"].mean()
else:
    churn_rate = 0
    average_age = 0
    average_balance = 0
    average_credit_score = 0

st.markdown("# Customer Churn Intelligence")
st.markdown(
    "Interactive dashboard for understanding customer retention "
    "and identifying major churn patterns."
)

st.markdown("---")

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

metric1.metric(
    "Customers",
    f"{total_customers:,}"
)

metric2.metric(
    "Churned",
    f"{churned_customers:,}"
)

metric3.metric(
    "Churn Rate",
    f"{churn_rate:.2f}%"
)

metric4.metric(
    "Avg Age",
    f"{average_age:.1f}"
)

metric5.metric(
    "Avg Credit Score",
    f"{average_credit_score:.0f}"
)

st.markdown("<br>", unsafe_allow_html=True)

overview_col1, overview_col2 = st.columns([1, 1.5])

with overview_col1:

    st.markdown(
        '<div class="section-title">Customer Retention</div>',
        unsafe_allow_html=True
    )

    churn_data = (
        filtered_df["Churn_Status"]
        .value_counts()
        .reset_index()
    )

    churn_data.columns = [
        "Status",
        "Customers"
    ]

    fig = px.pie(
        churn_data,
        names="Status",
        values="Customers",
        hole=0.65
    )

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        showlegend=True,
        margin=dict(l=10, r=10, t=30, b=10)
    )

    fig.update_traces(
        textinfo="percent",
        hovertemplate="%{label}<br>Customers: %{value}<extra></extra>"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with overview_col2:

    st.markdown(
        '<div class="section-title">Churn Rate by Geography</div>',
        unsafe_allow_html=True
    )

    geography_data = (
        filtered_df.groupby("Geography")["Exited"]
        .mean()
        .reset_index()
    )

    geography_data["Churn Rate"] = (
        geography_data["Exited"] * 100
    )

    geography_data = geography_data.sort_values(
        "Churn Rate"
    )

    fig = px.bar(
        geography_data,
        x="Churn Rate",
        y="Geography",
        orientation="h",
        text="Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            title="Churn Rate (%)",
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="",
            gridcolor="#24324A"
        ),
        margin=dict(l=20, r=50, t=30, b=30)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.markdown(
    '<div class="section-title">Customer Demographics</div>',
    unsafe_allow_html=True
)

demo_col1, demo_col2 = st.columns(2)

with demo_col1:

    gender_data = (
        filtered_df.groupby("Gender")["Exited"]
        .mean()
        .reset_index()
    )

    gender_data["Churn Rate"] = (
        gender_data["Exited"] * 100
    )

    fig = px.bar(
        gender_data,
        x="Gender",
        y="Churn Rate",
        text="Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        title="Churn Rate by Gender",
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Churn Rate (%)",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with demo_col2:

    active_data = (
        filtered_df.groupby("IsActiveMember")["Exited"]
        .mean()
        .reset_index()
    )

    active_data["Membership"] = active_data[
        "IsActiveMember"
    ].map({
        0: "Inactive",
        1: "Active"
    })

    active_data["Churn Rate"] = (
        active_data["Exited"] * 100
    )

    fig = px.bar(
        active_data,
        x="Membership",
        y="Churn Rate",
        text="Churn Rate"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        title="Churn Rate by Membership",
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Churn Rate (%)",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.markdown(
    '<div class="section-title">Customer Behaviour</div>',
    unsafe_allow_html=True
)

behaviour_col1, behaviour_col2 = st.columns(2)

with behaviour_col1:

    fig = px.histogram(
        filtered_df,
        x="Age",
        color="Churn_Status",
        nbins=30,
        barmode="overlay"
    )

    fig.update_layout(
        title="Age Distribution",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            title="Age",
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Customers",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with behaviour_col2:

    fig = px.histogram(
        filtered_df,
        x="Balance",
        color="Churn_Status",
        nbins=30,
        barmode="overlay"
    )

    fig.update_layout(
        title="Balance Distribution",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            title="Balance",
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Customers",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

factor_col1, factor_col2 = st.columns(2)

with factor_col1:

    product_data = (
        filtered_df.groupby("NumOfProducts")["Exited"]
        .agg(["mean", "count"])
        .reset_index()
    )

    product_data["Churn Rate"] = (
        product_data["mean"] * 100
    )

    fig = px.bar(
        product_data,
        x="NumOfProducts",
        y="Churn Rate",
        text="Churn Rate",
        hover_data=["count"]
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        title="Churn Rate by Number of Products",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            title="Number of Products",
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Churn Rate (%)",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with factor_col2:

    tenure_data = (
        filtered_df.groupby("Tenure")["Exited"]
        .mean()
        .reset_index()
    )

    tenure_data["Churn Rate"] = (
        tenure_data["Exited"] * 100
    )

    fig = px.line(
        tenure_data,
        x="Tenure",
        y="Churn Rate",
        markers=True
    )

    fig.update_layout(
        title="Churn Rate by Tenure",
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#CBD5E1"),
        xaxis=dict(
            title="Tenure",
            gridcolor="#24324A"
        ),
        yaxis=dict(
            title="Churn Rate (%)",
            gridcolor="#24324A"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.markdown(
    '<div class="section-title">Credit Score Analysis</div>',
    unsafe_allow_html=True
)

fig = px.histogram(
    filtered_df,
    x="CreditScore",
    color="Churn_Status",
    nbins=35,
    barmode="overlay"
)

fig.update_layout(
    height=420,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#CBD5E1"),
    xaxis=dict(
        title="Credit Score",
        gridcolor="#24324A"
    ),
    yaxis=dict(
        title="Customers",
        gridcolor="#24324A"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.markdown(
    '<div class="section-title">Correlation Analysis</div>',
    unsafe_allow_html=True
)

numeric_columns = [
    "CreditScore",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Exited"
]

correlation = filtered_df[
    numeric_columns
].corr()

fig = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto"
)

fig.update_layout(
    height=600,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#CBD5E1")
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.markdown(
    '<div class="section-title">Filtered Customer Records</div>',
    unsafe_allow_html=True
)

display_columns = [
    "CustomerId",
    "Surname",
    "CreditScore",
    "Geography",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "IsActiveMember",
    "EstimatedSalary",
    "Churn_Status"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

st.markdown(
    "Customer Churn Intelligence Dashboard | Bank Customer Churn Analysis"
)