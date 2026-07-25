from portfolio_lab.factors import AltmanZFactor
from portfolio_lab.models import FinancialStatement


def test_altman_score():

    statement = FinancialStatement(
        ticker="TEST",
        fiscal_year=2024,
        total_assets=1000,
        total_liabilities=500,
        current_assets=400,
        current_liabilities=200,
        retained_earnings=300,
        ebit=120,
        revenue=1800,
        market_cap=3500,
    )

    factor = AltmanZFactor()

    result = factor.calculate(statement)

    assert result.score > 3
    assert result.category == "Healthy"
    assert result.factor_name == "Altman Z"