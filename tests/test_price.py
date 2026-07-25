from datetime import datetime

from portfolio_lab.models import PriceData


def test_price_data():

    price = PriceData(
        ticker="TCS",
        timestamp=datetime.now(),
        open=3800,
        high=3850,
        low=3780,
        close=3840,
        adjusted_close=3840,
        volume=2500000,
    )

    assert price.close == 3840

    assert price.typical_price == (3850 + 3780 + 3840) / 3
