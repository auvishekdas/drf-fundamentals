from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
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

