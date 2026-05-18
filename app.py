import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Data Analytics Dashboard",
    layout="wide"
)

# TITLE
st.title("📊 Data Analytics Dashboard")
st.caption("Interactive Business Intelligence Dashboard")

st.markdown("---")

# FILE UPLOAD
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    # READ DATA
    df = pd.read_csv(uploaded_file)

    # DATA PREVIEW
    st.subheader("📂 Dataset Preview")
    st.dataframe(df.head())

    st.markdown("---")

    # KPI SECTION
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) > 0:
        total = df[numeric_cols[0]].sum()
        col3.metric(f"Total {numeric_cols[0]}", f"{total:,.2f}")

    st.markdown("---")

    # COLUMN SELECTION
    st.subheader("📈 Visualization")

    x_axis = st.selectbox("Select X-axis", df.columns)

    y_axis = st.selectbox(
        "Select Y-axis",
        numeric_cols
    )

    # CHART
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(df[x_axis].astype(str), df[y_axis])

    plt.xticks(rotation=45)

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)

    st.pyplot(fig)

    st.markdown("---")

    # FILTERING
    st.subheader("🔎 Filter Data")

    filter_column = st.selectbox(
        "Select column to filter",
        df.columns
    )

    unique_values = df[filter_column].unique()

    selected_value = st.selectbox(
        "Select value",
        unique_values
    )

    filtered_df = df[
        df[filter_column] == selected_value
    ]

    st.dataframe(filtered_df)

else:
    st.info("👆 Upload a CSV file to begin analysis")
