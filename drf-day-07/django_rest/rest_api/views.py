from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
#Queryset
def aiquest_info(request):
    #Complex data
    ai = Aiquest.objects.all()
    #Python dictionary
    serializer = AiquestSerializer(ai, many=True)
    #Render json
    json_data = JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data, content_type='application/json')

#Model instance
def aiquest_ins(request, pk):
    #Complex data
    ai = Aiquest.objects.get(id=pk)
    #Python dictionary
    serializer = AiquestSerializer(ai)
    #Render json
    json_data = JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data, content_type='application/json')
@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #python to complex
        serializer = AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Successfully Update data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application.json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application.json')
    
    if request.method == 'PUT':
        json_data = request.body
        #json to stream
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id = id)
        serializer = AiquestSerializer(aiq, data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Successfully Update data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json', status = 400)