from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey

from .models import Branch_table, faculty_table, section_table, semester_table, subjects_table



class sub_fac_relation(models.Model):
    branch_id = ForeignKey(Branch_table,on_delete=CASCADE)
    section = ForeignKey(section_table,on_delete=CASCADE)
    semester = ForeignKey(semester_table,on_delete=CASCADE)
    subject = ForeignKey(subjects_table,on_delete=CASCADE)
    faculty = ForeignKey(faculty_table,on_delete=CASCADE)