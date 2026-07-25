"""
Yahoo Finance data provider.
"""

from datetime import datetime

import yfinance as yf

from portfolio_lab.datasource.base_provider import BaseProvider
from portfolio_lab.models import PriceData
from portfolio_lab.utils import get_logger

logger = get_logger(__name__)


class YahooProvider(BaseProvider):

    def get_price_history(
        self,
        ticker: str,
        start_date: str,
        end_date: str,
    ) -> list[PriceData]:

        logger.info(f"Downloading {ticker} from Yahoo Finance")

        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False,
            auto_adjust=False,
        )
        if df.columns.nlevels > 1:
            df.columns = df.columns.get_level_values(0)

        prices: list[PriceData] = []

        for date, row in df.iterrows():

            prices.append(
                PriceData(
                    ticker=ticker,
                    timestamp=date.to_pydatetime(),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    adjusted_close=float(row["Adj Close"]),
                    volume=int(row["Volume"]),
                )
            )

        logger.info(f"Downloaded {len(prices)} candles.")

        return prices

    def get_latest_price(self, ticker: str) -> PriceData:

        prices = self.get_price_history(
            ticker=ticker,
            start_date="2025-01-01",
            end_date=datetime.today().strftime("%Y-%m-%d"),
        )

        return prices[-1]