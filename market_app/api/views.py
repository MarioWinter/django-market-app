from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer
from market_app.models import Market

from market_app.api import serializers

@api_view(['GET', 'POST'])
def markets_view(request):
    if request.method == "GET":
        markets = Market.objects.all()  # Es werden alle Market-Objekte aus der Datenbank abgerufen
        serializer = MarketSerializer(markets, many=True)  # Der Serializer wird auf die Liste der Market-Objekte angewendet
        return Response(serializer.data)  # Die serialisierten Daten werden als Response zurückgegeben
    if request.method == "POST":
        try:
            msg = request.data['message']
            name = request.data['name']
            return Response({"message": msg, "name": name}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)