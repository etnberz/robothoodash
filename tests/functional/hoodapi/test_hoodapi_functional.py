from pathlib import Path

import duckdb
import numpy as np
import pandas as pd
import pytest

from robothoodash.hoodapi.hoodapi import HoodApi

np.random.seed(42)

TEST_DATA_PATH = Path(__file__).parent.parent / "data"

TEST_DATA_TRACKER = pd.DataFrame(
    {
        "timestamp": pd.date_range(start="2023-05-25 00:00", freq="H", periods=24),
        "btc_balance": np.random.normal(loc=0.07, scale=0.004, size=24),
        "usdt_balance": np.random.normal(loc=1000, scale=20, size=24),
    }
)

TEST_DATA_ORDERS = pd.read_parquet(TEST_DATA_PATH / "open_order_test_data.parquet")


@pytest.mark.parametrize(
    "base_currency, tracker",
    [("btc", TEST_DATA_TRACKER), ("usdt", TEST_DATA_TRACKER)],
    ids=["BTC", "USDT"],
)
def test_get_balance_data_base_currency(
    mocker, tracker, base_currency
):  # pylint:disable=unused-argument
    mocker.patch("robothoodash.hoodapi.hoodapi.duckdb.connect", return_value=duckdb.connect())
    hood_api = HoodApi(base_currency=base_currency)
    result = hood_api.get_balance_data()
    expected_result = (
        TEST_DATA_TRACKER[["timestamp", "btc_balance"]]
        if base_currency == "btc"
        else TEST_DATA_TRACKER[["timestamp", "usdt_balance"]]
    )
    pd.testing.assert_frame_equal(left=result, right=expected_result)


@pytest.mark.parametrize(
    "base_currency, trading_signal",
    [("btc", TEST_DATA_ORDERS), ("usdt", TEST_DATA_ORDERS)],
    ids=["BTC", "USDT"],
)
def test_get_open_orders(mocker, base_currency, trading_signal):  # pylint:disable=unused-argument
    mocker.patch("robothoodash.hoodapi.hoodapi.duckdb.connect", return_value=duckdb.connect())
    hood_api = HoodApi(base_currency=base_currency)
    result = hood_api.get_open_orders()
    expected_result = trading_signal[
        (trading_signal["open"] == 1) & (trading_signal["base_currency"] == base_currency.upper())
    ][["pair", "quantity", "strategy", "target_1", "target_2", "status"]].reset_index(drop=True)
    pd.testing.assert_frame_equal(left=result, right=expected_result)
