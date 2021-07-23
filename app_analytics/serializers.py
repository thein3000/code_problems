from rest_framework import serializers


class OrderLineSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ("SHIPPED", "SHIPPED"),
        ("PENDING", "PENDING"),
        ("CANCELLED", "CANCELLED"),
    )
    order_number = serializers.CharField(max_length=20)
    item_name = serializers.CharField(max_length=200, write_only=True, required=False)
    status = serializers.ChoiceField(choices=STATUS_CHOICES)


class HistoricOrderSerializer(serializers.Serializer):
    ord_id = serializers.CharField(max_length=40)
    ord_dt = serializers.DateField(format="%m/%d/%y", input_formats=["%m/%d/%y"])
    qt_ordd = serializers.IntegerField()


class OrderSeasonSerializer(serializers.Serializer):
    SEASON_CHOICES = (
        ("Fall", "Fall"),
        ("Winter", "Winter"),
        ("Summer", "Summer"),
        ("Spring", "Spring"),
    )
    ord_id = serializers.CharField(max_length=40)
    season = serializers.ChoiceField(choices=SEASON_CHOICES)


class WeatherSerializer(serializers.Serializer):
    date = serializers.DateField(format="%d/%m/%y", input_formats=["%d/%m/%y"])
    was_rainy = serializers.BooleanField()
