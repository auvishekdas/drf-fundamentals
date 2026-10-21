from rest_framework import serializers
from . models import Aiquest

class AiquestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aiquest
        fields = ['id', 'student_name', 'class_name', 'seat']