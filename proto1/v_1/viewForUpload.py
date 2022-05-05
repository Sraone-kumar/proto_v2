
from django.shortcuts import redirect
from django.urls import reverse
import pandas as pd
from v_1 import uploadApi, models


def uploadBasic(request):

    if(bool(request.FILES)):
        if(request.POST.get('action') == 'subjects_table'):
            subjects_upload(request.FILES['upload'])
        if(request.POST.get('action') == 'faculty_table'):
            faculty_upload(request.FILES['upload'])

    # print(request.path)

    return redirect(to=reverse("admin:v_1_"+request.POST.get('action')+"_changelist"))


def subjects_upload(excel):
    pandasObj = pd.read_excel(excel)

    uploader = uploadApi.Upload(models.subjects_table, pandasObj)
    # WARNING parameters are columns names....if they change in excel or table may raise error
    uploader.uploadChecker('subject_code', 'subject_code')
    uploader.forienKeyConverter(
        models.semester_table, 'semester_number', 'semester_taught')
    uploader.forienKeyConverter(
        models.department_table, 'department_name', 'department_id')
    # uploader.printer()

    row_iter = uploader.PandasObject.iterrows()
    objs = [
        models.subjects_table(
            subject_code=row['subject_code'],
            subject_short_name=row['subject_short_name'],
            subject_name=row['subject_name'],
            subject_credits=row['subject_credits'],
            Elective_type=row['Elective_type'],
            semester_taught=row['semester_taught'],
            department_id=row['department_id']

        )
        for index, row in row_iter
    ]

    models.subjects_table.objects.bulk_create(objs)


def faculty_upload(excel):
    pandasObj = pd.read_excel(excel)

    uploader = uploadApi.Upload(models.faculty_table, pandasObj)

    uploader.uploadChecker('faculty_name', 'faculty_name')
    uploader.forienKeyConverter(
        models.department_table, 'department_name', 'Department_id')
    uploader.forienKeyConverter(
        models.Designation_table, 'designation_name', 'Designation_id')

    uploader.printer()

    row_iter = uploader.PandasObject.iterrows()
    objs = [
        models.faculty_table(
            faculty_id=row['faculty_id'],
            faculty_short_name=row['faculty_short_name'],
            faculty_name=row['faculty_name'],
            No_hrs_per_week=row['No_hrs_per_week'],
            Designation_id=row['Designation_id'],
            Department_id=row['Department_id']
        )

        for index, row in row_iter
    ]

    models.faculty_table.objects.bulk_create(objs)
