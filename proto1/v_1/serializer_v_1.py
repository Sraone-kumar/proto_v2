from rest_framework import serializers

from .sub_fac_model import sub_fac_relation
from .models import Block_table,Designation_table,department_table,class_time_table,Branch_table,faculty_table,subjects_table


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
        fields = ('subject_id','subject_name',)

class ClassTableSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    subject_id = SubjectsSerializer()
    class Meta:
        model = class_time_table
        fields = ('weekday_id','timing_id','semester','branch','section','subject_id')


class facultySerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_table
        fields = ('id','faculty_name')

class fac_relationSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    faculty = facultySerializer()
    class Meta:
        model = sub_fac_relation
        fields = ('subject','faculty')