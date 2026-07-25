from portfolio_lab.datasource import YahooProvider
from services import MarketDataService

provider = YahooProvider()

service = MarketDataService(provider)

prices = service.get_price_history(
    ticker="AAPL",
    start_date="2024-01-01",
    end_date="2025-01-01",
)

print(prices[0])
print(prices[-1])