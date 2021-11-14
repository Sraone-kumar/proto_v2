from django.db.models import fields
from rest_framework import serializers
from .models import Department_table,Designation_table


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation_table
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()
    class Meta:
        model = Department_table
        fields = ('id','department_name','designation')


