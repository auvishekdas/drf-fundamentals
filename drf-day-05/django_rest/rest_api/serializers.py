from rest_framework import serializers
from . models import Aiquest

class AiquestSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=30)
    class_name = serializers.CharField(max_length=15)
    seat = serializers.IntegerField()

    def create(self, validated_data):
        return Aiquest.objects.create(**validated_data)