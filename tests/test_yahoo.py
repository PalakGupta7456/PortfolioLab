from portfolio_lab.datasource import YahooProvider

provider = YahooProvider()

prices = provider.get_price_history(
    ticker="AAPL",
    start_date="2024-01-01",
    end_date="2025-01-01",
)

print(f"Downloaded {len(prices)} candles")

print()

print(prices[0])

print()

print(prices[-1])