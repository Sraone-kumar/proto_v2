from calendar import weekday
from v_1.models import class_time_table, lab_time_table


def constrainCheckForClass(faculty, week, time) -> bool:
    countOFClass = class_time_table.objects.filter(
        faculty_id=faculty, weekday_id=week, timing_id=time).count()
    if(countOFClass == 0):
        return False

    return True


# def constrainCheckForLab(val)->bool:
#     countOFClass = lab_time_table.objects.filter(faculty_id=faculty,weekday_id  = week,timing_id = time).count()
#     if(countOFClass == 0):
#         return False

#     return True;
