import requests
import os
from dotenv import load_dotenv
import pandas
from data.ticker_model import TickerModel

ENDPOINT = "https://www.alphavantage.co/query"

class StockManager:
    def __init__(self):
        load_dotenv()
        self.endpoint = ENDPOINT
        self.default_queries = {
            "function": "TIME_SERIES_DAILY",
            "apikey": os.environ.get("ALPHA_VANTAGE_API")
        }
        try:
            data = pandas.read_csv("data/tickers.csv")
            self.tickers = data["tickers"].tolist()
        except FileNotFoundError:
            self.tickers = ["nvda"]

    def add_ticker(self, ticker: str):
        self.tickers.append(ticker)

        new_ticker = pandas.Series(ticker, name="tickers")
        new_ticker.to_csv("data/tickers.csv", index=False, header=False, mode="a")

    def fetch_ticker(self, ticker: str):
        self.default_queries["symbol"] = ticker
        response = requests.get(url=self.endpoint, params=self.default_queries)
        response.raise_for_status()

        ticker_data = response.json()["Time Series (Daily)"]
        date_keys = list(ticker_data.keys())

        latest_data = ticker_data[date_keys[0]]
        previous_data = ticker_data[date_keys[1]]
        growth_rate = (float(latest_data["4. close"]) - float(previous_data["4. close"])) / float(
            previous_data["4. close"])

        return TickerModel(
            symbol=ticker,
            growth_rate=growth_rate,
            latest_data=latest_data,
            previous_data=previous_data
        )

    def stocks_over_5pct_change(self, tickers=None) -> list[TickerModel]:
        if not tickers:
            tickers = self.tickers

        high_change_stocks = []

        for ticker in tickers:
            ticker_data = self.fetch_ticker(ticker)
            if ticker_data.growth_rate*100>= 5 or ticker_data.growth_rate*100 <= -5:
                high_change_stocks.append(ticker_data)

        return high_change_stocks