from pathlib import Path

import duckdb
import pandas as pd
import pytest

from robothoodash.hoodapi.sql_queries import (
    GET_BTC_BALANCE_TS,
    GET_BTC_OPEN_ORDERS,
    GET_USDT_BALANCE_TS,
    GET_USDT_OPEN_ORDERS,
    HOODAPI_QUERIES,
)

# Mock DuckDB connection for testing

TEST_DATA = Path(__file__).parent.parent / "functional" / "data" / "open_order_test_data.parquet"


class MockDuckDBConnection:
    def __init__(self):
        self.data = {
            GET_BTC_BALANCE_TS: pd.DataFrame(
                {"timestamp": [1, 2, 3], "btc_balance": [0.5, 0.6, 0.7]}
            ),
            GET_USDT_BALANCE_TS: pd.DataFrame(
                {"timestamp": [1, 2, 3], "usdt_balance": [1000, 1200, 1500]}
            ),
            GET_BTC_OPEN_ORDERS: pd.read_parquet(TEST_DATA),
            GET_USDT_OPEN_ORDERS: pd.read_parquet(TEST_DATA),
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
