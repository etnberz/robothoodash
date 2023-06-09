import os

import duckdb
import pandas as pd

from robothoodash.hoodapi.sql_queries import (
    GET_BTC_BALANCE_TS,
    GET_BTC_OPEN_ORDERS,
    GET_BTC_PROFIT_DAY,
    GET_BTC_PROFIT_MONTH,
    GET_BTC_PROFIT_WEEK,
    GET_USDT_BALANCE_TS,
    GET_USDT_OPEN_ORDERS,
    GET_USDT_PROFIT_DAY,
    GET_USDT_PROFIT_MONTH,
    GET_USDT_PROFIT_WEEK,
)

# pylint:disable=unused-variable,too-few-public-methods


ALLOWED_BASE_CURRENCY = ["btc", "usdt"]


class HoodApi:
    """The API to request the data we need with the DuckDB connector"""

    def __init__(self, base_currency: str = "btc") -> None:
        """Init HoodApi

        Parameters
        ----------
        base_currency: str
            Name of the base currency

        Raises
        ------
        ValueError
            If base_currency is not provided with the allowed values
        """

        if base_currency not in ALLOWED_BASE_CURRENCY:
            raise ValueError(
                f"base_currency should take one of the following values: {ALLOWED_BASE_CURRENCY}"
            )

        self.con = duckdb.connect(os.environ["ROBOTHOOD_DB_PATH"])
        self.base_currency = base_currency

    def get_balance_data(self) -> pd.DataFrame:
        """Get balance data for a given base currency

        Returns
        -------
        pd.DataFrame
            The time series of the balance data as a dataframe

        """
        query = GET_BTC_BALANCE_TS if self.base_currency == "btc" else GET_USDT_BALANCE_TS
        return self.con.execute(query=query).df()

    def get_open_orders(self) -> pd.DataFrame:
        """Get open trading orders for a given base currency

        Returns
        -------
        pd.DataFrame
            The open trading orders as a dataframe

        """
        query = GET_BTC_OPEN_ORDERS if self.base_currency == "btc" else GET_USDT_OPEN_ORDERS
        return self.con.execute(query=query).df()

    def get_profit(self, granularity: str) -> pd.DataFrame:
        """Get open trading orders for a given base currency

        Returns
        -------
        pd.DataFrame
            The open trading orders as a dataframe

        """
        if granularity == "month":
            query = GET_BTC_PROFIT_MONTH if self.base_currency == "btc" else GET_USDT_PROFIT_MONTH
        elif granularity == "week":
            query = GET_BTC_PROFIT_WEEK if self.base_currency == "btc" else GET_USDT_PROFIT_WEEK
        else:
            query = GET_BTC_PROFIT_DAY if self.base_currency == "btc" else GET_USDT_PROFIT_DAY
        return self.con.execute(query=query).df()
