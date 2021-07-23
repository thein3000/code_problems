from django.utils import timezone
import datetime as dt
import itertools
import copy


def detect_weather_changes(data):
    # TODO: Implement logic
    return [
        {
            "date": timezone.now().date(),
            "was_rainy": True
        }
    ]


def identify_order_status(data):
    """Given a list of order lines from a common order, returns the overall status."""
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    CANCELLED = "CANCELLED"

    status_counts = {
        SHIPPED: 0,
        PENDING: 0,
        CANCELLED: 0
    }
    for order in data:
        if order["status"] == SHIPPED:
            status_counts[SHIPPED] += 1
        elif order["status"] == PENDING:
            status_counts[PENDING] += 1
        else:
            status_counts[CANCELLED] += 1

    if status_counts[PENDING] > 0:
        return PENDING
    elif status_counts[CANCELLED] > 0 and status_counts[SHIPPED] == 0:
        return CANCELLED
    return SHIPPED


def identify_multiple_order_status(data):
    """Given a list of order lines, returns the orders with the respective overall status."""
    order_line_list = copy.deepcopy(data)
    order_list = []

    key_func = lambda x: x["order_number"]

    for key, group in itertools.groupby(order_line_list, key_func):
        order_list.append({
            "order_number": key,
            "status": identify_order_status(group)
        })
    return order_list


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
