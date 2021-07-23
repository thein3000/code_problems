from django.utils import timezone


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


def identify_multiple_order_season(data):
    return [
        {
            "ord_id": "1133-342342342342",
            "season": "Fall"
        }
    ]