from django.db.models import fields
from rest_framework import serializers

from .sub_fac_model import sub_fac_relation
from .models import Block_table,Designation_table,department_table,class_time_table,Branch_table,faculty_table,subjects_table,lab_information_table,lab_time_table


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


class facultySerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_table
        fields = ('id','faculty_name')

class ClassTableSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    subject_id = SubjectsSerializer()
    faculty_id = facultySerializer()
    class Meta:
        model = class_time_table
        fields = ('weekday_id','timing_id','semester','branch','section','subject_id','faculty_id')




class fac_relationSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    faculty = facultySerializer()
    class Meta:
        model = sub_fac_relation
        fields = ('subject','faculty')

class Lab_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_information_table
        fields = ('lab_id','lab_name')


class LabTableSerializer(serializers.ModelSerializer):
    lab = Lab_infoSerializer()
    lab_course = SubjectsSerializer()
    lab_faculty = facultySerializer()
    class Meta:
        model = lab_time_table
        fields = ('id','lab','lab_course','lab_faculty','no_of_hours','time','week')
    
class SubFacSerializer(serializers.ModelSerializer):
    subject= SubjectsSerializer()
    faculty = facultySerializer()
    class Meta:
        model = sub_fac_relation
        fields = ('id','subject','faculty')