import duckdb
import pandas as pd


class DuckDBManager:
    """
    Manages the DuckDB database used by the application.
    """

    def __init__(self, database_path: str = "data/assistant.duckdb"):
        self.database_path = database_path

        self.connection = duckdb.connect(
            database_path
        )

    def load_dataframe(
        self,
        df: pd.DataFrame,
        table_name: str = "sales",
    ) -> None:
        """
        Create or replace a DuckDB table from a DataFrame.
        """

        self.connection.register(
            "uploaded_dataframe",
            df,
        )

        self.connection.execute(
            f"""
            CREATE OR REPLACE TABLE {table_name}
            AS
            SELECT *
            FROM uploaded_dataframe
            """
        )

        self.connection.unregister(
            "uploaded_dataframe"
        )

    def execute_query(
        self,
        query: str,
    ) -> pd.DataFrame:
        """
        Execute a SQL query and return the result
        as a Pandas DataFrame.
        """

        result = self.connection.execute(
            query
        ).df()

        return result

    def get_schema(
        self,
        table_name: str = "sales",
    ) -> pd.DataFrame:
        """
        Return the table schema from DuckDB.
        """

        return self.connection.execute(
            f"""
            DESCRIBE {table_name}
            """
        ).df()

    def close(self) -> None:
        """
        Close the DuckDB connection.
        """

        self.connection.close()