"""
Represents the output of a factor calculation.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class FactorResult:
    """
    Result returned by a financial factor.
    """

    ticker: str

    factor_name: str

    score: float

    category: str

    components: dict[str, float] = field(default_factory=dict)