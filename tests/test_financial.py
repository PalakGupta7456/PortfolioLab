from portfolio_lab.models import FinancialStatement


def test_financial_statement():

    statement = FinancialStatement(
        ticker="AAPL",
        fiscal_year=2024,
        total_assets=1000,
        total_liabilities=600,
        current_assets=300,
        current_liabilities=200,
        retained_earnings=250,
        ebit=150,
        revenue=1200,
        market_cap=2500,
    )

    assert statement.ticker == "AAPL"