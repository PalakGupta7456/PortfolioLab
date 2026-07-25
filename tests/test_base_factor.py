from portfolio_lab.factors import BaseFactor


def test_base_factor_is_abstract():

    try:
        BaseFactor()
        assert False

    except TypeError:
        assert True