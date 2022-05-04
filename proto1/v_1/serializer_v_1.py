from django.db.models import fields
from rest_framework import serializers

from .sub_fac_model import sub_fac_relation
from .models import Block_table, Designation_table, department_table, class_time_table, Branch_table, faculty_table, section_table, semester_table, subjects_table, lab_information_table, lab_time_table


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section_table
        fields = ('section_id', 'section_number')


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = semester_table
        fields = ('semester_id', 'semester_number')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block_table
        fields = ('block_name',)


class BranchSerializer(serializers.ModelSerializer):
    block_id = BlockSerializer()

    class Meta:
        model = Branch_table
        fields = ('branch_name', 'block_id')


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects_table
        fields = ('subject_id', 'subject_code',
                  'subject_name', 'subject_short_name')


class facultySerializer(serializers.ModelSerializer):
    class Meta:
        model = faculty_table
        fields = ('id', 'faculty_name', 'faculty_short_name')


class ClassTableSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    subject_id = SubjectsSerializer()
    faculty_id = facultySerializer()
    section = SectionSerializer()
    semester = SemesterSerializer()

    class Meta:
        model = class_time_table
        fields = ('weekday_id', 'timing_id', 'semester',
                  'branch', 'section', 'subject_id', 'faculty_id')


class fac_relationSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    faculty = facultySerializer()

    class Meta:
        model = sub_fac_relation
        fields = ('subject', 'faculty')


class Lab_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_information_table
        fields = ('lab_id', 'lab_name', 'lab_short_name')


class LabTableSerializer(serializers.ModelSerializer):
    lab = Lab_infoSerializer()
    lab_course = SubjectsSerializer()
    lab_faculty = facultySerializer()
    section = SectionSerializer()
    branch = BranchSerializer()
    semester = SemesterSerializer()

    class Meta:
        model = lab_time_table
        fields = ('id', 'lab', 'lab_course', 'lab_faculty', 'no_of_hours',
                  'time', 'week', 'branch', 'section', 'semester')


class SubFacSerializer(serializers.ModelSerializer):
    subject = SubjectsSerializer()
    faculty = facultySerializer()

    class Meta:
        model = sub_fac_relation
        fields = ('id', 'subject', 'faculty')
