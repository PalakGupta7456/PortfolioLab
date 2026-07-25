"""
Implementation of the Altman Z-Score.
"""

from portfolio_lab.factors import BaseFactor
from portfolio_lab.models import FinancialStatement
from portfolio_lab.models.factor_result import FactorResult


class AltmanZFactor(BaseFactor):
    """
    Calculates the Altman Z-Score.
    """

    def calculate(self, statement: FinancialStatement) -> float:

        working_capital = (
            statement.current_assets
            - statement.current_liabilities
        )

        a = working_capital / statement.total_assets

        b = (
            statement.retained_earnings
            / statement.total_assets
        )

        c = (
            statement.ebit
            / statement.total_assets
        )

        d = (
            statement.market_cap
            / statement.total_liabilities
        )

        e = (
            statement.revenue
            / statement.total_assets
        )

        z_score = (
            1.2 * a
            + 1.4 * b
            + 3.3 * c
            + 0.6 * d
            + 1.0 * e
        )

        return FactorResult(
            ticker=statement.ticker,
            factor_name="Altman Z",
            score=z_score,
            category=self._classify(z_score),
            components={
                "A": a,
                "B": b,
                "C": c,
                "D": d,
                "E": e,
            },
)
    def _classify(self, score: float) -> str:
        """
        Classify the Altman Z-Score.
        """

        if score < 1.8:
            return "Distress"

        if score < 3.0:
            return "Grey Zone"

        return "Healthy"