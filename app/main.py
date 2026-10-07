import streamlit as st

from app.services.data_service import DataService
from app.database.duckdb_manager import DuckDBManager


st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide",
)


st.title("🤖 AI SQL Assistant")

st.write(
    "Upload a CSV or Excel file and explore your data."
)


# --------------------------------------------------
# Create services
# --------------------------------------------------

data_service = DataService()


# --------------------------------------------------
# File uploader
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"],
)


# --------------------------------------------------
# Process uploaded file
# --------------------------------------------------

if uploaded_file is not None:

    try:

        # Load file into Pandas
        df = data_service.load_file(
            uploaded_file
        )

        # Display success message
        st.success(
            f"{uploaded_file.name} uploaded successfully."
        )

        # ------------------------------------------
        # Dataset information
        # ------------------------------------------

        st.subheader("Dataset Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Rows",
                len(df),
            )

        with col2:
            st.metric(
                "Columns",
                len(df.columns),
            )


        # ------------------------------------------
        # Dataset preview
        # ------------------------------------------

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(5),
            use_container_width=True,
        )

        # ------------------------------------------
        # Schema
        # ------------------------------------------

        st.subheader("Dataset Schema")

        schema = data_service.get_schema(
            df
        )

        st.dataframe(
            schema,
            use_container_width=True,
        )

        # ------------------------------------------
        # DuckDB
        # ------------------------------------------

        db = DuckDBManager()

        db.load_dataframe(
            df,
            table_name="sales",
        )

        st.success(
            "Dataset successfully loaded into DuckDB."
        )

        # ------------------------------------------
        # Test SQL query
        # ------------------------------------------

        st.subheader(
            "Database Test"
        )

        result = db.execute_query(
            """
            SELECT COUNT(*) AS total_rows
            FROM sales
            """
        )

        st.write(
            "Total rows inside DuckDB:"
        )

        st.dataframe(
            result
        )

        # ------------------------------------------
        # DuckDB schema
        # ------------------------------------------

        st.subheader(
            "DuckDB Table Schema"
        )

        duckdb_schema = db.get_schema(
            "sales"
        )

        st.dataframe(
            duckdb_schema,
            use_container_width=True,
        )

        db.close()

    except Exception as error:

        st.error(
            f"Error processing file: {error}"
        )