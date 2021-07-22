from rest_framework.views import APIView
from rest_framework.response import Response


class SeasonDetectionView(APIView):

    def post(self, request):
        return Response({"season": "one"})

class OrderStatusView(APIView):

    def post(self, request):
        return Response({"order": "one"})

class WeatherChangeView(APIView):
    
    def post(self, request):
        return Response({"weather": "one"})