from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def aiquest_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            #complex data
            ai = Aiquest.objects.get(id=id)
            #python dictionary
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)

        #complex data
        ai = Aiquest.objects.all()
        #python dictionary
        serializer = AiquestSerializer(ai, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AiquestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully insert data'})
        return Response(serializer.errors)
    

