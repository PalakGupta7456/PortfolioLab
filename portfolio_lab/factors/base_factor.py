"""
Abstract base class for all financial factors.
"""

from abc import ABC, abstractmethod


class BaseFactor(ABC):
    """
    Base interface for factor calculations.
    """

    @abstractmethod
    def calculate(self, *args, **kwargs):
        """
        Calculate the factor value.
        """
        raise NotImplementedError