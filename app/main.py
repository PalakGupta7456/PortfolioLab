from portfolio_lab.config import settings
from portfolio_lab.utils import get_logger

logger = get_logger(__name__)


def main():
    logger.info("Starting PortfolioLab")

    print("=" * 60)
    print(settings.PROJECT_NAME)
    print(settings.VERSION)
    print("=" * 60)

    logger.info("Application initialized successfully")


if __name__ == "__main__":
    main()