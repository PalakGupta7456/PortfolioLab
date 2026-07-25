"""
Abstract base class for all market data providers.
"""

from abc import ABC, abstractmethod

from portfolio_lab.models import PriceData


class BaseProvider(ABC):
    """
    Interface for all market data providers.
    """

    @abstractmethod
    def get_price_history(
        self,
        ticker: str,
        start_date: str,
        end_date: str,
    ) -> list[PriceData]:
        """
        Return historical market data.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest_price(
        self,
        ticker: str,
    ) -> PriceData:
        """
        Return the latest available market data.
        """
        raise NotImplementedError