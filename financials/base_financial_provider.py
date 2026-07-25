"""
Abstract interface for financial statement providers.
"""

from abc import ABC, abstractmethod

from portfolio_lab.models import FinancialStatement


class BaseFinancialProvider(ABC):

    @abstractmethod
    def get_financial_statement(
        self,
        ticker: str,
    ) -> FinancialStatement:
        """
        Returns the latest financial statement.
        """
        raise NotImplementedError