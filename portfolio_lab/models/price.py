"""
Data model representing market price data.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class PriceData:
    """
    Represents one OHLCV record for a stock.
    """

    ticker: str

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    adjusted_close: float

    volume: int

    @property
    def typical_price(self) -> float:
        """
        Returns the typical price used in technical analysis.
        """
        return (self.high + self.low + self.close) / 3

    def __post_init__(self):
        if self.high < self.low:
            raise ValueError("High price cannot be less than low price.")

        if self.volume < 0:
            raise ValueError("Volume cannot be negative.")