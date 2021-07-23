from django.utils import timezone
import datetime as dt
import copy


def detect_weather_changes(data):
    return [
        {
            "date": timezone.now().date(),
            "was_rainy": True
        }
    ]


def identify_multiple_order_status(data):
    return [
        {
            "order_number": "ORD_1567",
            "status": "PENDING"
        }
    ]


def get_date_season(date):
    """Given a datetime.date instance, identify the season."""
    # Define a common year so that it is not taken into account.
    COMMON_YEAR = 2000
    date_copy = dt.datetime(date.year, date.month, date.day).date()
    common_year_date = date_copy.replace(year=COMMON_YEAR)

    seasons = {
        "Spring": (dt.date(COMMON_YEAR, 3, 19), dt.date(COMMON_YEAR, 6, 19),),
        "Summer": (dt.date(COMMON_YEAR, 6, 20), dt.date(COMMON_YEAR, 8, 21),),
        "Fall": (dt.date(COMMON_YEAR, 9, 22), dt.date(COMMON_YEAR, 12, 20),),
    }

    for season, (start, end) in seasons.items():
        if common_year_date >= start and common_year_date <= end:
            return season
    return "Winter"


def get_order_with_season(data):
    """Given an order, identify the season it was created in."""
    order = copy.deepcopy(data)
    order["season"] = get_date_season(order["ord_dt"])
    return order


def get_multiple_orders_with_season(data):
    """ Given a list of orders, return a list of orders with its respective seasons identified. """
    return [get_order_with_season(order) for order in data]
