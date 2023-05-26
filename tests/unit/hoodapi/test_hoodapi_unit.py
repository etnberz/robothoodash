import pandas as pd
import pytest

from robothoodash.hoodapi.hoodapi import ALLOWED_BASE_CURRENCY, HoodApi


@pytest.mark.parametrize("base_currency", ALLOWED_BASE_CURRENCY, ids=ALLOWED_BASE_CURRENCY)
def test_get_balance_data_valid_base_currency(
    mock_duckdb_connection, base_currency
):  # pylint:disable=unused-argument
    hood_api = HoodApi()
    result = hood_api.get_balance_data(base_currency=base_currency)
    assert isinstance(result, pd.DataFrame)


def test_get_balance_data_invalid_base_currency(
    mock_duckdb_connection,
):  # pylint:disable=unused-argument
    hood_api = HoodApi()
    with pytest.raises(ValueError):
        hood_api.get_balance_data("invalid_currency")
