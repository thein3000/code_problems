  
from app_analytics.views import OrderStatusView, SeasonDetectionView, WeatherChangeView
from django.urls import path

urlpatterns = [
    path(f'weather_change/', WeatherChangeView.as_view()),
    path(f'order_status/', OrderStatusView.as_view()),
    path(f'season_detection/', SeasonDetectionView.as_view()),
]