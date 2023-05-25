import os

import duckdb
import pandas as pd

# pylint:disable=unused-variable,too-few-public-methods


class HoodApi:
    """The API to request the data we need with the DuckDB connector"""

    def __init__(self) -> None:
        duckdb.load_extension(extension="sqlite_scanner")
        self.con = duckdb.connect(os.environ["ROBOTHOOD_DB_PATH"])

    def get_balance_data(self, base_currency: str) -> pd.DataFrame:
        """Get balance data for a given base currency (BTC or USDT)

        Parameters
        ----------
        base_currency: str
            Name of the base currency

        Returns
        -------
        pd.DataFrame
            The time series of the balance data as a dataframe

        """
        return self.con.sql(f"""SELECT timestamp, {base_currency}_balance FROM tracker""").df()
