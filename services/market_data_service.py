"""
Market Data Service.

Acts as the single entry point for all market data.
"""

from portfolio_lab.datasource import BaseProvider
from portfolio_lab.models import PriceData


class MarketDataService:

    def __init__(self, provider: BaseProvider):

        self.provider = provider

    def get_price_history(
        self,
        ticker: str,
        start_date: str,
        end_date: str,
    ) -> list[PriceData]:

        return self.provider.get_price_history(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date,
        )

    def get_latest_price(
        self,
        ticker: str,
    ) -> PriceData:

        return self.provider.get_latest_price(ticker)