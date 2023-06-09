# pylint:disable=unused-variable

GET_BTC_BALANCE_TS = """SELECT timestamp, btc_balance FROM tracker"""
GET_USDT_BALANCE_TS = """SELECT timestamp, usdt_balance FROM tracker"""
GET_USDT_OPEN_ORDERS = """SELECT pair, quantity, strategy, target_1, target_2, status
                     FROM trading_signal WHERE open AND base_currency = 'USDT'"""
GET_BTC_OPEN_ORDERS = """SELECT pair, quantity, strategy, target_1, target_2, status
                     FROM trading_signal WHERE open AND base_currency = 'BTC'"""

GET_BTC_PROFIT_MONTH = """SELECT
               STRPTIME(timestr, '%b - %Y') AS period,
               SUM(diff) AS btc_profit
               FROM (
                    SELECT
                    btc_balance - LAG(btc_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%b - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period"""

GET_USDT_PROFIT_MONTH = """SELECT
               STRPTIME(timestr, '%b - %Y') AS period,
               SUM(diff) AS usdt_profit
               FROM (
                    SELECT
                    usdt_balance - LAG(usdt_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%b - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period"""

GET_BTC_PROFIT_WEEK = """SELECT
               STRPTIME(timestr, '%W - %Y') AS period,
               SUM(diff) AS btc_profit
               FROM (
                    SELECT
                    btc_balance - LAG(btc_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%W - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period"""

GET_USDT_PROFIT_WEEK = """SELECT
               STRPTIME(timestr, '%W - %Y') AS period,
               SUM(diff) AS usdt_profit
               FROM (
                    SELECT
                    usdt_balance - LAG(usdt_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%W - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period"""


GET_BTC_PROFIT_DAY = """SELECT
               STRPTIME(timestr, '%d - %m - %Y')AS period,
               SUM(diff) AS btc_profit
               FROM (
                    SELECT
                    btc_balance - LAG(btc_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%d - %m - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period
               """

GET_USDT_PROFIT_DAY = """SELECT
               STRPTIME(timestr, '%d - %m - %Y')AS period,
               SUM(diff) AS usdt_profit
               FROM (
                    SELECT
                    usdt_balance - LAG(usdt_balance) over (ORDER BY timestamp) AS diff,
                    STRFTIME(timestamp, '%d - %m - %Y') AS timestr
                    FROM tracker
                    )
               GROUP BY period
               ORDER BY period"""

HOODAPI_QUERIES = [
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
]
