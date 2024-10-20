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
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.erros)