from pathlib import Path

import duckdb
import pandas as pd
import pytest

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
    HOODAPI_QUERIES,
)

# Mock DuckDB connection for testing

TEST_DATA = Path(__file__).parent.parent / "functional" / "data" / "open_order_test_data.parquet"
btc_profit_data = pd.DataFrame({"period": [1, 2, 3], "btc_profit": [0.5, 0.6, 0.7]})
usdt_profit_data = pd.DataFrame({"period": [1, 2, 3], "usdt_profit": [0.5, 0.6, 0.7]})


class MockDuckDBConnection:
    def __init__(self):
        open_orders = pd.read_parquet(TEST_DATA)
        self.data = {
            GET_BTC_BALANCE_TS: pd.DataFrame(
                {"timestamp": [1, 2, 3], "btc_balance": [0.5, 0.6, 0.7]}
            ),
            GET_USDT_BALANCE_TS: pd.DataFrame(
                {"timestamp": [1, 2, 3], "usdt_balance": [1000, 1200, 1500]}
            ),
            GET_BTC_OPEN_ORDERS: open_orders[open_orders["base_currency"] == "BTC"],
            GET_USDT_OPEN_ORDERS: open_orders[open_orders["base_currency"] == "USDT"],
            GET_BTC_PROFIT_DAY: btc_profit_data,
            GET_BTC_PROFIT_MONTH: btc_profit_data,
            GET_BTC_PROFIT_WEEK: btc_profit_data,
            GET_USDT_PROFIT_DAY: usdt_profit_data,
            GET_USDT_PROFIT_MONTH: usdt_profit_data,
            GET_USDT_PROFIT_WEEK: usdt_profit_data,
        }

    def execute(self, query):
        if query in HOODAPI_QUERIES:
            return MockDuckDBPyConnection(data=self.data[query], query=query)
        raise ValueError("Invalid query")


class MockDuckDBPyConnection:
    def __init__(self, data, query):
        self.data = data
        self.query = query

    def df(self):  # pylint:disable=disallowed-name
        return self.data


@pytest.fixture
def mock_duckdb_connection(monkeypatch):
    def mock_connect(*args, **kwargs):  # pylint:disable=unused-argument
        return MockDuckDBConnection()

    monkeypatch.setattr(duckdb, "connect", mock_connect)
