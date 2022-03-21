
from django.shortcuts import redirect
from django.urls import reverse
import pandas as pd
from v_1 import uploadApi, models


def uploadBasic(request):

    if(bool(request.FILES)):
        if(request.POST.get('action') == 'subjects_table'):
            subjects_upload(request.FILES['upload'])

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
            subject_name=row['subject_name'],
            subject_credits=row['subject_credits'],
            Elective_type=row['Elective_type'],
            semester_taught=row['semester_taught'],
            department_id=row['department_id']

        )
        for index, row in row_iter
    ]

    models.subjects_table.objects.bulk_create(objs)
