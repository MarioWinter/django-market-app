from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


from .serializers import MarketSerializer, SellerSerializer, ProductsSerializer, MarketHyperlinkedSerializer
from market_app.models import Market, Seller, Product

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from market_app.api import serializers


#class based view lowest
class MarketsView(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketHyperlinkedSerializer


class MarketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer




#function based height
@api_view(['GET', 'POST'])
def markets_view(request):
    if request.method == "GET":
        markets = Market.objects.all()  # Es werden alle Market-Objekte aus der Datenbank abgerufen
        serializer = MarketHyperlinkedSerializer(markets, many=True, context={'request': request})  # Der Serializer wird auf die Liste der Market-Objekte angewendet
        return Response(serializer.data)  # Die serialisierten Daten werden als Response zurückgegeben
    
          
    if request.method == "POST":  # Prüft, ob die HTTP-Methode POST ist
        serializer = MarketSerializer(data=request.data)  # Erstellt einen Serializer mit den Daten aus der Anfrage
        if serializer.is_valid():  # Überprüft, ob die Daten gültig sind (entsprechend den Regeln im Serializer)
            serializer.save()  # Speichert die Daten in der Datenbank (erstellt ein neues Market-Objekt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Gibt die gespeicherten Daten als Antwort zurück
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Gibt Fehlermeldungen zurück, wenn die Daten ungültig sind


#function based height
@api_view(['GET','PUT', 'DELETE'])  # Dekorator, der angibt, dass diese View GET und DELETE Anfragen akzeptiert
def single_market_view(request, pk):  # pk = primary Key, ist die ID aus der Datenbank
    try:
        market = Market.objects.get(pk=pk)  # Versucht, das Market-Objekt mit der gegebenen ID zu finden
    except Market.DoesNotExist:  # Fängt den Fall ab, wenn kein Objekt mit dieser ID existiert
        return Response(status=status.HTTP_404_NOT_FOUND)  # Gibt 404 Not Found zurück, wenn das Objekt nicht existiert
        
    if request.method == "GET":  # Wenn die Anfrage eine GET-Anfrage ist
        serializer = MarketSerializer(market, context={'request': request})  # Serialisiert das gefundene Market-Objekt
        return Response(serializer.data)  # Gibt die serialisierten Daten als Antwort zurück
    
    elif request.method == "PUT":  # Prüft, ob die HTTP-Methode PUT ist (für Aktualisierungen)
        serializer = MarketSerializer(market, data=request.data, partial=True)  # Erstellt einen Serializer mit dem existierenden Objekt und den neuen Daten, erlaubt partielle Updates
        if serializer.is_valid():  # Überprüft, ob die neuen Daten gültig sind
            serializer.save()  # Aktualisiert das existierende Market-Objekt mit den neuen Daten
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Gibt die aktualisierten Daten und einen 201 Status zurück
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Gibt Fehlermeldungen zurück, wenn die Daten ungültig sind

    elif request.method == "DELETE":  # Wenn die Anfrage eine DELETE-Anfrage ist
        market.delete()  # Löscht das Market-Objekt aus der Datenbank
        return Response(status=status.HTTP_204_NO_CONTENT)  # Gibt 204 No Content zurück, um erfolgreiche Löschung anzuzeigen
    
#function based height
@api_view(['GET', 'POST'])
def sellers_view(request):
    if request.method == "GET":
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)#gibt alle verkäufer zurück
        return Response(serializer.data)
    
          
    if request.method == "POST":  # Prüft, ob die HTTP-Methode POST ist
        serializer = SellerSerializer(data=request.data)  # Erstellt einen Serializer mit den Daten aus der Anfrage
        if serializer.is_valid():  # Überprüft, ob die Daten gültig sind (entsprechend den Regeln im Serializer)
            serializer.save()  # Speichert die Daten in der Datenbank (erstellt ein neues Market-Objekt)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Gibt die gespeicherten Daten als Antwort zurück
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Gibt Fehlermeldungen zurück, wenn die Daten ungültig sind


#function based height
@api_view(['GET','PUT', 'DELETE'])  # Dekorator, der angibt, dass diese View GET und DELETE Anfragen akzeptiert
def single_sellers_view(request, pk):  # pk = primary Key, ist die ID aus der Datenbank
    try:
        seller = Seller.objects.get(pk=pk)  # Versucht, das Market-Objekt mit der gegebenen ID zu finden
    except Seller.DoesNotExist:  # Fängt den Fall ab, wenn kein Objekt mit dieser ID existiert
        return Response(status=status.HTTP_404_NOT_FOUND)  # Gibt 404 Not Found zurück, wenn das Objekt nicht existiert
        
    if request.method == "GET":  # Wenn die Anfrage eine GET-Anfrage ist
        serializer = SellerSerializer(seller)  # Serialisiert das gefundene Market-Objekt
        return Response(serializer.data)  # Gibt die serialisierten Daten als Antwort zurück
    
    elif request.method == "PUT":  # Prüft, ob die HTTP-Methode PUT ist (für Aktualisierungen)
        serializer = SellerSerializer(seller, data=request.data, partial=False)  # Erstellt einen Serializer mit dem existierenden Objekt und den neuen Daten, erlaubt partielle Updates
        if serializer.is_valid():  # Überprüft, ob die neuen Daten gültig sind
            serializer.save()  # Aktualisiert das existierende Market-Objekt mit den neuen Daten
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Gibt die aktualisierten Daten und einen 201 Status zurück
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Gibt Fehlermeldungen zurück, wenn die Daten ungültig sind

    elif request.method == "DELETE":  # Wenn die Anfrage eine DELETE-Anfrage ist
        seller.delete()  # Löscht das Market-Objekt aus der Datenbank
        return Response(status=status.HTTP_204_NO_CONTENT)  # Gibt 204 No Content zurück, um erfolgreiche Löschung anzuzeigen

#ModelViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    


#viewSet
class ProductViewSetOld(viewsets.ViewSet):
    queryset = Product.objects.all()
    
    def list(self, request):#all GET
        serializer = ProductsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):#single object GET
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def create(self, request):#all POST
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None): #single PUT
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductsSerializer(product, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None): #single PATCH
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None): #single DELETE
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = ProductsSerializer(product)
        product.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    






#class based view height
class ProductView(APIView):
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#function based height
@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



 #function based height   
@api_view(['GET','PUT', 'DELETE'])  # Dekorator, der angibt, dass diese View GET und DELETE Anfragen akzeptiert
def single_product_view(request, pk):  # pk = primary Key, ist die ID aus der Datenbank
    try:
        product = Product.objects.get(pk=pk)  # Versucht, das Market-Objekt mit der gegebenen ID zu finden
    except Product.DoesNotExist:  # Fängt den Fall ab, wenn kein Objekt mit dieser ID existiert
        return Response(status=status.HTTP_404_NOT_FOUND)  # Gibt 404 Not Found zurück, wenn das Objekt nicht existiert
        
    if request.method == "GET":  # Wenn die Anfrage eine GET-Anfrage ist
        serializer = ProductsSerializer(product)  # Serialisiert das gefundene Market-Objekt
        return Response(serializer.data)  # Gibt die serialisierten Daten als Antwort zurück
    
    elif request.method == "PUT":  # Prüft, ob die HTTP-Methode PUT ist (für Aktualisierungen)
        serializer = ProductsSerializer(product, data=request.data, partial=True)  # Erstellt einen Serializer mit dem existierenden Objekt und den neuen Daten, erlaubt partielle Updates
        if serializer.is_valid():  # Überprüft, ob die neuen Daten gültig sind
            serializer.save()  # Aktualisiert das existierende Market-Objekt mit den neuen Daten
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Gibt die aktualisierten Daten und einen 201 Status zurück
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Gibt Fehlermeldungen zurück, wenn die Daten ungültig sind

    elif request.method == "DELETE":  # Wenn die Anfrage eine DELETE-Anfrage ist
        product.delete()  # Löscht das Market-Objekt aus der Datenbank
        return Response(status=status.HTTP_204_NO_CONTENT)  # Gibt 204 No Content zurück, um erfolgreiche Löschung anzuzeigen
    