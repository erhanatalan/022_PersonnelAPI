from rest_framework import serializers
from .models import Department, Personnel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Department
        fields = '__all__'
        
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        models = Personnel
        fields = ('first_name', 'last_name', 'title')
        
class DepartmentPersonnelSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(many=True, read_only=True)
    class Meta:
        models = Department
        fields = ('id', 'name', 'personnel')
