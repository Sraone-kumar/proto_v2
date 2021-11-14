from django.contrib import admin
from .models import subjects_table,Designation_table,department_table, faculty_table, class_time_table,Timings_table,Block_table,Week_table,Room_table,Branch_table

admin.site.register(subjects_table)
admin.site.register(Designation_table)
admin.site.register(department_table)
admin.site.register(faculty_table)
admin.site.register(class_time_table)
admin.site.register(Timings_table)
admin.site.register(Block_table)
admin.site.register(Week_table)
admin.site.register(Room_table)
admin.site.register(Branch_table)
# Register your models here.
