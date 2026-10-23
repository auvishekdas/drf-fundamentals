'''
from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
'''
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
# Create your views here.
class Aiquest_Model_View_Set(viewsets.ModelViewSet):
    queryset = Aiquest.objects.all()   
    serializer_class = AiquestSerializer 
    permission_classes = [IsAdminUser]
    
 
    
'''
class AiquestCreate(APIView):
    def get(self, request, pk=None, format=None):
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

    def post(self, request, format=None):
        serializer = AiquestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully insert data'})
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(pk = id)
        serializer = AiquestSerializer(ai, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Full data updated'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
            id = pk
            ai = Aiquest.objects.get(pk = id)
            serializer = AiquestSerializer(ai, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Partial data updated'})
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(pk = id)
        ai.delete()
        return Response({'message': 'Successfully deleted data'})
    
'''