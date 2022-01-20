import json
from .models import class_time_table, faculty_table

def check_fac(request):
    # vals = class_time_table.objects.all().values("faculty_id_id")
    vals = faculty_table.objects.all().values('id','faculty_id','faculty_name')
    for i in vals:
        print(i)
    # print("its here")
    # print(list(vals))