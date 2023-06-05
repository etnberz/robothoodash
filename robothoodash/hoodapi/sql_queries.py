# pylint:disable=unused-variable

GET_BTC_BALANCE_TS = """SELECT timestamp, btc_balance FROM tracker"""
GET_USDT_BALANCE_TS = """SELECT timestamp, usdt_balance FROM tracker"""
GET_USDT_OPEN_ORDERS = """SELECT pair, quantity, strategy, target_1, target_2, status
                     FROM trading_signal WHERE open AND base_currency = 'USDT'"""
GET_BTC_OPEN_ORDERS = """SELECT pair, quantity, strategy, target_1, target_2, status
                     FROM trading_signal WHERE open AND base_currency = 'BTC'"""

HOODAPI_QUERIES = [
    GET_BTC_BALANCE_TS,
    GET_USDT_BALANCE_TS,
    GET_BTC_OPEN_ORDERS,
    GET_USDT_OPEN_ORDERS,
]
