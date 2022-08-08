from django.contrib import admin
from .models import Default_class_Room, Manual_class_room, lab_information_table, lab_time_table, subjects_table, Designation_table, department_table, faculty_table, class_time_table, Timings_table, Block_table, Week_table, Room_table, Branch_table, semester_table, section_table, Editors
from .sub_fac_model import sub_fac_relation


class facAdmin(admin.ModelAdmin):
    list_display = ('id', 'faculty_id', 'faculty_name',
                    'No_hrs_per_week', 'Designation_id', 'Department_id')
    search_fields = ('faculty_name', 'Department_id__department_name',)
    list_filter = ('Department_id',)
    change_list_template = 'change_list_upload.html'


class subAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'semester_taught', 'department_id')
    change_list_template = 'change_list_upload.html'


class classAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'faculty_id', 'branch', 'weekday_id', 'timing_id',
                    'section', 'semester', 'Room_with_block')
    search_fields = ('weekday_id_id__week_name', 'timing_id')
    list_filter = ('weekday_id',)


class subFacAdmin(admin.ModelAdmin):
    list_display = ('branch_id', 'section', 'semester', 'subject', 'faculty')


class LabFacAdmin(admin.ModelAdmin):
    list_display = ('lab', 'lab_course', 'lab_faculty', 'week',
                    'time', 'branch', 'section', 'semester', 'no_of_hours')


class EditorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'password')


class DefaultClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'semester', 'section', 'room')


class ManualClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'semester', 'section',
                    'weekday', 'timing', 'manual_class', 'no_of_hours')


admin.site.register(subjects_table, subAdmin)
admin.site.register(Designation_table)
admin.site.register(department_table)
admin.site.register(faculty_table, facAdmin)
admin.site.register(class_time_table, classAdmin)
admin.site.register(Timings_table)
admin.site.register(Block_table)
admin.site.register(Week_table)
admin.site.register(Room_table)
admin.site.register(Branch_table)
admin.site.register(section_table)
admin.site.register(semester_table)
admin.site.register(sub_fac_relation, subFacAdmin)
admin.site.register(lab_information_table)
admin.site.register(lab_time_table, LabFacAdmin)
admin.site.register(Editors, EditorsAdmin)
admin.site.register(Default_class_Room, DefaultClassRoomAdmin)
admin.site.register(Manual_class_room, ManualClassAdmin)
# Register your models here.
