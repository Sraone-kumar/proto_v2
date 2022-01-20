from django.contrib import admin
from .models import lab_information_table, lab_time_table, subjects_table,Designation_table,department_table, faculty_table, class_time_table,Timings_table,Block_table,Week_table,Room_table,Branch_table,semester_table,section_table,Editors
from .sub_fac_model import sub_fac_relation

class subAdmin(admin.ModelAdmin):
    list_display = ('subject_name','semester_taught','department_id')


class classAdmin(admin.ModelAdmin):
    list_display = ('subject_id','faculty_id','branch','section','semester','Room_with_block')

class subFacAdmin(admin.ModelAdmin):
    list_display = ('branch_id','section','semester','subject','faculty')

class LabFacAdmin(admin.ModelAdmin):
    list_display = ('lab','lab_course','lab_faculty','week','time','branch','section','semester','no_of_hours')

class EditorsAdmin(admin.ModelAdmin):
    list_display = ('id','user','password')

admin.site.register(subjects_table,subAdmin)
admin.site.register(Designation_table)
admin.site.register(department_table)
admin.site.register(faculty_table)
admin.site.register(class_time_table,classAdmin)
admin.site.register(Timings_table)
admin.site.register(Block_table)
admin.site.register(Week_table)
admin.site.register(Room_table)
admin.site.register(Branch_table)
admin.site.register(section_table)
admin.site.register(semester_table)
admin.site.register(sub_fac_relation,subFacAdmin)
admin.site.register(lab_information_table)
admin.site.register(lab_time_table,LabFacAdmin)
admin.site.register(Editors,EditorsAdmin)
# Register your models here.
