from financials import BaseFinancialProvider


def test_base_financial_provider():

    try:
        BaseFinancialProvider()
        assert False

    except TypeError:
        assert True