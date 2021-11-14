from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Designation_table(models.Model):
    designation_name = CharField(max_length=30)

    def __str__(self) -> str:
        return self.designation_name

class Department_table(models.Model):
    department_name = CharField(max_length=50)
    designation = ForeignKey(Designation_table,on_delete=CASCADE)

    def __str__(self) -> str:
        return self.department_name





