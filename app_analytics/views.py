from app_analytics.analytics_engine.core import detect_weather_changes, identify_multiple_order_status, \
    identify_multiple_order_season
from app_analytics.serializers import WeatherSerializer, HistoricOrderSerializer, OrderLineSerializer, \
    OrderSeasonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SeasonDetectionView(APIView):

    def post(self, request):
        serializer = HistoricOrderSerializer(data=request.data, many=True)
        if serializer.is_valid():
            analyzed_data = identify_multiple_order_season(serializer.validated_data)
            response_serializer = OrderSeasonSerializer(data=analyzed_data, many=True)
            if response_serializer.is_valid():
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderStatusView(APIView):

    def post(self, request):
        serializer = OrderLineSerializer(data=request.data, many=True)
        if serializer.is_valid():
            analyzed_data = identify_multiple_order_status(serializer.validated_data)
            response_serializer = OrderLineSerializer(data=analyzed_data, many=True)
            if response_serializer.is_valid():
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherChangeView(APIView):
    
    def post(self, request):
        serializer = WeatherSerializer(data=request.data, many=True)
        if serializer.is_valid():
            analyzed_data = detect_weather_changes(serializer.validated_data)
            response_serializer = WeatherSerializer(data=analyzed_data, many=True)
            if response_serializer.is_valid():
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)