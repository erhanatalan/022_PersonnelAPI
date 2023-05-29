from rest_framework import serializers
from .models import Department, Personnel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Department
        fields = '__all__'
        
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Personnel
        fields = '__all__'
