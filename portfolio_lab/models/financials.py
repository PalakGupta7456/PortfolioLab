"""
Financial statement data model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class FinancialStatement:
    """
    Represents the financial statement data required
    for factor calculations.
    """

    ticker: str

    fiscal_year: int

    total_assets: float

    total_liabilities: float

    current_assets: float

    current_liabilities: float

    retained_earnings: float

    ebit: float

    revenue: float

    market_cap: float