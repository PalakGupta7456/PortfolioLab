from portfolio_lab.config import settings


def main():

    print("=" * 60)
    print(settings.PROJECT_NAME)
    print(settings.VERSION)
    print("=" * 60)

    print()

    print("Root Directory")
    print(settings.ROOT_DIR)

    print()

    print("Data Directory")
    print(settings.DATA_DIR)

    print()

    print("Risk Free Rate")
    print(settings.RISK_FREE_RATE)

    print()

    print("Trading Days")
    print(settings.TRADING_DAYS)


if __name__ == "__main__":
    main()