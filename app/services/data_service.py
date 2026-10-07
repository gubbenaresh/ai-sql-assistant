from io import BytesIO

import pandas as pd


class DataService:
    """
    Handles loading CSV and Excel files into Pandas DataFrames.
    """

    SUPPORTED_EXTENSIONS = [".csv", ".xlsx"]

    def load_file(self, uploaded_file) -> pd.DataFrame:
        """
        Load an uploaded CSV or Excel file into a DataFrame.
        """

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(
                uploaded_file,
                engine="openpyxl",
            )

        else:
            raise ValueError(
                "Unsupported file type. "
                "Please upload CSV or XLSX."
            )

        if df.empty:
            raise ValueError(
                "The uploaded file contains no data."
            )

        return df

    def get_file_info(self, df: pd.DataFrame) -> dict:
        """
        Return basic information about the dataset.
        """

        return {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
        }

    def get_schema(self, df: pd.DataFrame) -> list[dict]:
        """
        Return column names and Pandas data types.
        """

        schema = []

        for column in df.columns:
            schema.append(
                {
                    "column": column,
                    "dtype": str(df[column].dtype),
                }
            )

        return schema