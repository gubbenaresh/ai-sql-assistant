import pandas as pd

from app.database.duckdb_manager import DuckDBManager
from app.services.data_service import DataService


def test_load_sample_data():

    df = pd.read_csv(
        "data/sample_sales.csv"
    )

    assert not df.empty

    assert len(df) == 20

    assert "Product" in df.columns

    assert "Region" in df.columns

    assert "Sales_Amount" in df.columns

    db = DataService()

    db.get_file_info(df)
    
    db.get_schema(df)

def test_load_dataframe_into_duckdb():

    df = pd.read_csv(
        "data/sample_sales.csv"
    )

    db = DuckDBManager(
        "data/test_assistant.duckdb"
    )

    db.load_dataframe(
        df,
        "sales",
    )

    result = db.execute_query(
        """
        SELECT COUNT(*) AS total_rows
        FROM sales
        """
    )

    assert result.iloc[0]["total_rows"] == 20

    db.close()