import duckdb
import numpy as np
import pandas as pd
import pytest

from robothoodash.hoodapi.hoodapi import HoodApi

np.random.seed(42)

TEST_DATA = pd.DataFrame(
    {
        "timestamp": pd.date_range(start="2023-05-25 00:00", freq="H", periods=24),
        "btc_balance": np.random.normal(loc=0.07, scale=0.004, size=24),
        "usdt_balance": np.random.normal(loc=1000, scale=20, size=24),
    }
)


@pytest.mark.parametrize(
    "base_currency, tracker", [("btc", TEST_DATA), ("usdt", TEST_DATA)], ids=["BTC", "USDT"]
)
def test_get_balance_data_base_currency(
    mocker, tracker, base_currency
):  # pylint:disable=unused-argument
    mocker.patch("robothoodash.hoodapi.hoodapi.duckdb.connect", return_value=duckdb.connect())
    hood_api = HoodApi()
    result = hood_api.get_balance_data(base_currency=base_currency)
    expected_result = (
        TEST_DATA[["timestamp", "btc_balance"]]
        if base_currency == "btc"
        else TEST_DATA[["timestamp", "usdt_balance"]]
    )
    pd.testing.assert_frame_equal(left=result, right=expected_result)
