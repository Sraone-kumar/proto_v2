from statistics import mode
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
#independent tables................



class Timings_table(models.Model):
    timing_id  = IntegerField(primary_key=True)
    timing_space = CharField(max_length=255)

    def __str__(self) -> str:
        return self.timing_space


class section_table(models.Model):
    section_id = AutoField(primary_key=True)
    section_number = IntegerField()
    def __str__(self) -> str:
        return str(self.section_number)

class semester_table(models.Model):
    semester_id = AutoField(primary_key=True)
    semester_number = IntegerField()

    def __str__(self) -> str:
        return str(self.semester_number)

class Block_table(models.Model):
    block_id = IntegerField(primary_key=True)
    block_name = CharField(max_length=50)

    def __str__(self) -> str:
        return self.block_name

class Week_table(models.Model):
    week_id = IntegerField(primary_key=True)
    week_name = CharField(max_length=30)

    def __str__(self) -> str:
        return self.week_name


class Designation_table(models.Model):
    designation_id = IntegerField(primary_key=True)
    designation_name = CharField(max_length=50)

    def __str__(self) -> str:
        return self.designation_name

class department_table(models.Model):
    department_id = IntegerField(primary_key=True)
    department_name = CharField(max_length=100)

    def __str__(self) -> str:
        return self.department_name



#independent tables close---------------------------------------



class Room_table(models.Model):
    room_id = IntegerField(primary_key=True)
    class_number = IntegerField()
    block_id = ForeignKey(Block_table,on_delete=CASCADE)

    def __str__(self) -> str:
        return "{} : {}".format(self.block_id.block_name,self.class_number)


class Branch_table(models.Model):
    branch_id = IntegerField(primary_key=True)
    branch_name = CharField(max_length=30)
    block_id = ForeignKey(Block_table,on_delete=CASCADE)
    department_id = ForeignKey(department_table,on_delete=CASCADE)

    def __str__(self) -> str:
        return self.branch_name

class subjects_table(models.Model):
    subject_id = AutoField(primary_key=True)
    subject_code = CharField(max_length=30)
    subject_name = CharField(max_length=200)
    subject_credits = IntegerField()
    Elective_type = CharField(max_length=50)
    semester_taught = ForeignKey(semester_table,on_delete=CASCADE)
    department_id = ForeignKey(department_table,on_delete=CASCADE)

    def __str__(self) -> str:
        return self.subject_name


class faculty_table(models.Model):
    id = AutoField(primary_key=True)
    faculty_id = IntegerField(unique=True)
    faculty_name = CharField(max_length=100)
    No_hrs_per_week = IntegerField()
    Designation_id = models.ForeignKey(Designation_table, on_delete=CASCADE)
    Department_id = models.ForeignKey(department_table, on_delete=CASCADE)
    
    def __str__(self) -> str:
        return self.faculty_name




class class_time_table(models.Model):
    id = AutoField(primary_key=True)
    subject_id = models.ForeignKey(subjects_table,null=True, on_delete=CASCADE)
    faculty_id = ForeignKey(faculty_table,null=True, on_delete=CASCADE)
    weekday_id = ForeignKey(Week_table,on_delete=CASCADE)
    timing_id = ForeignKey(Timings_table,on_delete=CASCADE)
    Room_with_block = ForeignKey(Room_table,on_delete=CASCADE)
    branch = ForeignKey(Branch_table,on_delete=CASCADE)
    section = IntegerField()
    semester = IntegerField()




class lab_information_table(models.Model):
    lab_id = AutoField(primary_key=True)
    lab_name = CharField(max_length=300)
    lab_incharge = ForeignKey(faculty_table,on_delete=CASCADE)
    lab_assistant = ForeignKey(faculty_table,on_delete=CASCADE,related_name='lab_assistant')
    lab_department = ForeignKey(department_table,on_delete=CASCADE)
    lab_block = ForeignKey(Room_table,on_delete=CASCADE)

    def __str__(self) -> str:
        return self.lab_name

class lab_time_table(models.Model):
    id = AutoField(primary_key=True)
    lab = ForeignKey(lab_information_table,on_delete=CASCADE,null=True)
    lab_course = ForeignKey(subjects_table,on_delete=CASCADE,null=True)
    lab_faculty = ForeignKey(faculty_table,on_delete=CASCADE,null=True)
    week = ForeignKey(Week_table,on_delete=CASCADE)
    time = ForeignKey(Timings_table,on_delete=CASCADE)
    branch = ForeignKey(Branch_table,on_delete=CASCADE)
    section = ForeignKey(section_table,on_delete=CASCADE)
    semester = ForeignKey(semester_table,on_delete=CASCADE)
    no_of_hours = IntegerField(null=True)


class Editors(models.Model):
    id = AutoField(primary_key=True)
    user = ForeignKey(faculty_table,on_delete=CASCADE)
    password = CharField(max_length=300)





