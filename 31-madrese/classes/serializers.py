from rest_framework import serializers
from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['capacity', 'name', 'department', 'area']

    def validate_capacity(self, capacity):
        if capacity < 5:
            raise serializers.ValidationError("Capacity must be greater than or equal to 5")
        return capacity
        
    def validate_area(self, area):
        if area < 0:
            raise serializers.ValidationError("Area can't be negative")
        return area