#!/usr/bin/env python
from urllib.request import urlopen

import json
import os

API_KEY = os.environ.get("API_KEY")

STOCKS = [
    "AAPL", "MSFT",
    # "NVDA", "GOOG", "AMZN", "META",
    # "LLY", "XOM", "HD", "CVX",
    # "TSLA", "WMT", "MA", "PG", "ABBV", "KO",
    # "ADBE", "PEP",
    # "JPM", "V", "UNH", "JNJ", "ORCL", "COST", "BAC", "MRK", "NFLX",
    # "TMO", "CRM", "LIN"
]
START_DATE = "2019-09-10"
END_DATE = "2024-09-10"


def market_cap_api(stocks: list[str]):
    stocks_str = ",".join(stocks)
    url = "https://financialmodelingprep.com/api/v3/market-capitalization/{}?apikey={}".format(
        stocks_str, API_KEY)
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def historical_market_cap_api(stock: str, _from: str, to: str, limit: int):
    url = "https://financialmodelingprep.com/api/v3/historical-price-full/{}?limit={}&from={}&to={}&apikey={}".format(
        stock, limit, _from, to, API_KEY)
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


tab1, tab2 = [], []


def dump_csv(tab: list, filename: str):
    import csv
    with open(filename, mode="w", newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=tab[0].keys())
        writer.writeheader()
        for row in tab:
            writer.writerow(row)


def main():
    tab2_id = 0
    # collect data and setup 2 tabs
    for i in range(0, len(STOCKS), 5):
        batch = STOCKS[i:i+5]
        data_tab1_list = market_cap_api(batch)
        data_tab2_list = [historical_market_cap_api(
            x, START_DATE, END_DATE, 100000) for x in batch]
        data_tab1_map = {data["symbol"]: data for data in data_tab1_list}
        for data_tab2 in data_tab2_list:
            print(data_tab2)
            tab2.append(
                {"id": tab2_id, "ticker": data_tab2["symbol"], "data": data_tab2["historical"]})
            symbol = data_tab2["symbol"]
            tab1.append(
                {"ticker": symbol, "market_cap": data_tab1_map[symbol]["marketCap"], "pointer": tab2_id})
            tab2_id += 1
    dump_csv(tab1, "output/table1.csv")
    dump_csv(tab2, "output/table2.csv")
    # sort table1 by lexicographical order
    tab1.sort(key=lambda x: x["ticker"])
    dump_csv(tab1, "output/table1_sorted_a.csv")
    # sort table1 by market_cap
    tab1.sort(key=lambda x: int(x["market_cap"]))
    dump_csv(tab1, "output/table1_sorted_b.csv")


if __name__ == "__main__":
    main()
