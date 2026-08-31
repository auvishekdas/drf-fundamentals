from rest_framework import serializers

class AiquestSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=30)
    class_name = serializers.CharField(max_length=15)
    seat = serializers.IntegerField()
