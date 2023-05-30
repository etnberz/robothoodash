import os

import duckdb
import pandas as pd

# pylint:disable=unused-variable,too-few-public-methods

ALLOWED_BASE_CURRENCY = ["btc", "usdt"]

GET_BTC_BALANCE_TS = """SELECT timestamp, btc_balance FROM tracker"""
GET_USDT_BALANCE_TS = """SELECT timestamp, usdt_balance FROM tracker"""
GET_OPEN_ORDERS = """SELECT pair, quantity, strategy, target_1, target_2, status
                     FROM trading_signal WHERE open"""


class HoodApi:
    """The API to request the data we need with the DuckDB connector"""

    def __init__(self) -> None:
        self.con = duckdb.connect(os.environ["ROBOTHOOD_DB_PATH"])

    def get_balance_data(self, base_currency: str) -> pd.DataFrame:
        """Get balance data for a given base currency

        Parameters
        ----------
        base_currency: str
            Name of the base currency

        Raises
        ------
        ValueError
            If base_currency is not provided with the allowed values

        Returns
        -------
        pd.DataFrame
            The time series of the balance data as a dataframe

        """
        if base_currency not in ALLOWED_BASE_CURRENCY:
            raise ValueError(
                f"base_currency should take one of the following values: {ALLOWED_BASE_CURRENCY}"
            )
        query = GET_BTC_BALANCE_TS if base_currency == "btc" else GET_USDT_BALANCE_TS
        return self.con.execute(query=query).df()

    def get_open_orders(self) -> pd.DataFrame:
        """Get open trading orders

        Returns
        -------
        pd.DataFrame
            The open trading orders as a dataframe

        """
        return self.con.execute(query=GET_OPEN_ORDERS).df()
