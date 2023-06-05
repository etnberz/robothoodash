import pytest

from robothoodash.hoodapi.hoodapi import ALLOWED_BASE_CURRENCY, HoodApi


@pytest.mark.parametrize("base_currency", ALLOWED_BASE_CURRENCY, ids=ALLOWED_BASE_CURRENCY)
def test_hoodapi_init_valid_base_currency(
    mock_duckdb_connection, base_currency
):  # pylint:disable=unused-argument
    HoodApi(base_currency=base_currency)


def test_hoodapi_init_invalid_base_currency(
    mock_duckdb_connection,
):  # pylint:disable=unused-argument
    with pytest.raises(ValueError):
        HoodApi(base_currency="invalid_currency")
