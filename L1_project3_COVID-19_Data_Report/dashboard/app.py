import streamlit as st
import pandas as pd


#styling 

st.markdown("""
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


.stApp p {
    color: #1F2937;
}


.stApp label {
    color: #1F2937;
}


div[data-baseweb="select"] {
    background-color: #FFFFFF;
    color: #1F2937;
}


[data-testid="stMetric"] {
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


div[data-baseweb="select"] > div {
    background-color: #FFFFFF;
    border: 1px solid #B8CCE0;
    color: #1F2937;
}


div[data-baseweb="popover"] {
    background-color: #FFFFFF;
}

div[data-baseweb="popover"] * {
    color: #1F2937;
    background-color: #FFFFFF;
}


div[data-baseweb="option"] {
    color: #1F2937;
    background-color: #FFFFFF;
}


div[data-baseweb="option"]:hover {
    background-color: #EAF3FF;
    color: #0B5ED7;
}
</style>
""", unsafe_allow_html=True)

# 1. Page Title


st.title("COVID-19 Data Analysis Dashboard")

st.write(
    "This dashboard presents COVID-19 trends "
    "and country-level comparisons."
)



# 2. Load Dataset


df = pd.read_csv("./data/full_grouped.csv")




df["Date"] = pd.to_datetime(df["Date"])



# 3. Country Selector


countries = sorted(
    df["Country/Region"].unique()
)

selected_country = st.selectbox(
    "Select a country",
    countries
)


# 4. Filter Selected Country


country_data = df[
    df["Country/Region"] == selected_country
].sort_values("Date").copy()





latest = country_data.iloc[-1]



# 6. Display Latest Numbers


st.subheader("Latest Reported Data")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Confirmed",
    f"{latest['Confirmed']:,}"
)

col2.metric(
    "Deaths",
    f"{latest['Deaths']:,}"
)

col3.metric(
    "Recovered",
    f"{latest['Recovered']:,}"
)

col4.metric(
    "Active",
    f"{latest['Active']:,}"
)



# 7. Calculate Rolling Average


country_data["rolling_cases"] = (
    country_data["New cases"]
    .rolling(7)
    .mean()
)



# 8. Confirmed Cases Chart

st.subheader("Confirmed Cases")

st.line_chart(
    country_data,
    x="Date",
    y="Confirmed"
)


# 9. Active Cases Chart


st.subheader("Active Cases")

st.line_chart(
    country_data,
    x="Date",
    y="Active"
)


# 10. Recovered Cases Chart


st.subheader("Recovered Cases")

st.line_chart(
    country_data,
    x="Date",
    y="Recovered"
)


# 11. Deaths Chart


st.subheader("Deaths")

st.line_chart(
    country_data,
    x="Date",
    y="Deaths"
)



# 12. Daily Cases and Rolling Average


st.subheader(
    "Daily New Cases and 7-Day Rolling Average"
)

st.line_chart(
    country_data,
    x="Date",
    y=["New cases", "rolling_cases"]
)