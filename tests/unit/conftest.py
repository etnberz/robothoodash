import os

import duckdb
import pandas as pd
import pytest

from robothoodash.hoodapi.hoodapi import GET_BTC_BALANCE_TS, GET_USDT_BALANCE_TS


def pytest_configure(config):
    config.addinivalue_line("markers", "no_env_var: mark test to not use env var mock")


@pytest.fixture(autouse=True)
def mock_env_variables(request):
    if not request.node.get_closest_marker("no_profiling"):
        os.environ["ROBOTHOOD_DB_PATH"] = ""
    yield


# Mock DuckDB connection for testing
class MockDuckDBConnection:
    def __init__(self):
        self.data = {
            GET_BTC_BALANCE_TS: MockDuckDBPyConnection(
                pd.DataFrame({"timestamp": [1, 2, 3], "btc_balance": [0.5, 0.6, 0.7]})
            ),
            GET_USDT_BALANCE_TS: MockDuckDBPyConnection(
                pd.DataFrame({"timestamp": [1, 2, 3], "usdt_balance": [1000, 1200, 1500]})
            ),
        }

    def execute(self, query):
        if query in self.data:
            return self.data[query]
        raise ValueError("Invalid query")


class MockDuckDBPyConnection:
    def __init__(self, data):
        self.data = data

    def df(self):  # pylint:disable=disallowed-name
        return self.data


@pytest.fixture
def mock_duckdb_connection(monkeypatch):
    def mock_connect(*args, **kwargs):  # pylint:disable=unused-argument
        return MockDuckDBConnection()

    monkeypatch.setattr(duckdb, "connect", mock_connect)
