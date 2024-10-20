from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def first_view(request):
    if request.method == "GET":
        return Response({"message": "Hello, world!", "name":"Mario"})
    if request.method == "POST":
        try:
            msg = request.data['message']
            name = request.data['name']
            return Response({"message": msg, "name": name}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)