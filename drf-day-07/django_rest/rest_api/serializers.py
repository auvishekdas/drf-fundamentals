from rest_framework import serializers
from . models import Aiquest

class AiquestSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=30)
    class_name = serializers.CharField(max_length=15)
    seat = serializers.IntegerField()

    def create(self, validated_data):
        return Aiquest.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.student_name = validated_data.get('student_name',instance.student_name)
        instance.class_name = validated_data.get('class_name',instance.class_name)
        instance.seat = validated_data.get('seat',instance.seat)

        instance.save()
        return instance
