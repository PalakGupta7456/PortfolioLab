from portfolio_lab.datasource import BaseProvider


def test_base_provider_is_abstract():
    try:
        BaseProvider()
        assert False
    except TypeError:
        assert True