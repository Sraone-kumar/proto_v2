from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Block_table,Designation_table,department_table,class_time_table,Branch_table,subjects_table


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block_table
        fields = ('block_name',)



class BranchSerializer(serializers.ModelSerializer):
    block_id = BlockSerializer()
    class Meta:
        model = Branch_table
        fields = ('branch_name','block_id')

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects_table
        fields = ('subject_name',)

class ClassTableSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    subject_id = SubjectsSerializer()
    class Meta:
        model = class_time_table
        fields = ('weekday_id','timing_id','semester','branch','section','subject_id')