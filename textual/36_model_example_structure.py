# models/ticker.py
from dataclasses import dataclass
import csv
from typing import List

@dataclass
class Ticker:
    symbol: str
    price: str

    @staticmethod
    def save_to_csv(filename: str, data: List["Ticker"]):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["symbol", "price"])
            for item in data:
                writer.writerow([item.symbol, item.price])

    @staticmethod
    def load_from_csv(filename: str) -> List["Ticker"]:
        tickers = []
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tickers.append(Ticker(**row))
        return tickers
