"""
Application configuration for PortfolioLab.

This module contains all project-wide configuration values.
Any configuration that may be reused across multiple modules
should be defined here.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """
    Global application settings.

    Attributes
    ----------
    PROJECT_NAME : str
        Name of the project.

    VERSION : str
        Current application version.

    ROOT_DIR : Path
        Root directory of the project.

    DATA_DIR : Path
        Directory for storing datasets.

    CACHE_DIR : Path
        Directory for cached API responses.

    REPORT_DIR : Path
        Directory where reports are generated.

    LOG_DIR : Path
        Directory for log files.

    DEFAULT_UNIVERSE : str
        Default stock universe.

    TRADING_DAYS : int
        Number of trading days in a year.

    RISK_FREE_RATE : float
        Annual risk-free rate.

    MAX_PORTFOLIO_SIZE : int
        Maximum number of stocks in a portfolio.
    """

    PROJECT_NAME: str = "PortfolioLab"

    VERSION: str = "0.1.0"

    ROOT_DIR: Path = Path(__file__).resolve().parents[2]

    DATA_DIR: Path = ROOT_DIR / "data"

    CACHE_DIR: Path = DATA_DIR / "cache"

    REPORT_DIR: Path = ROOT_DIR / "reports"

    LOG_DIR: Path = ROOT_DIR / "logs"

    DEFAULT_UNIVERSE: str = "NIFTY500"

    TRADING_DAYS: int = 252

    RISK_FREE_RATE: float = 0.065

    MAX_PORTFOLIO_SIZE: int = 30


settings = Settings()

settings.LOG_DIR.mkdir(exist_ok=True)
settings.DATA_DIR.mkdir(exist_ok=True)
settings.CACHE_DIR.mkdir(exist_ok=True)
settings.REPORT_DIR.mkdir(exist_ok=True)