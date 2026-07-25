from portfolio_lab.factors import AltmanZFactor
from portfolio_lab.models import FinancialStatement

statement = FinancialStatement(
    ticker="AAPL",
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

print(f"Ticker : {statement.ticker}")
#print(f"Altman Z Score : {score:.2f}")

print(result.score)

print(result.category)

print(result.components)