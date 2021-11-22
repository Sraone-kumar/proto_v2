from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer_v_1 import fac_relationSerializer, facultySerializer

from .sub_fac_model import sub_fac_relation

from .models import faculty_table, subjects_table

def sub_fac(request):
    return render(request,'sub_fac_editor.html')


def get_info(request):
    if(request.GET.get('action') == 'info'):
        department = request.GET.get('department')
        semester  = request.GET.get('semester')
        faculty = list(faculty_table.objects.filter(Department_id_id = department).values('id','faculty_name'))
        #There should be condition for 1,2,3 semester subjects--which can be from
        #different departments
        courses = list(subjects_table.objects.filter(semester_taught_id = semester).values('subject_id','subject_name'))
        print(faculty)
        print(courses)
    if(request.GET.get('action') == 'submit'):
        submit_func(request)
        return JsonResponse({'success':'success'})
    return JsonResponse({'values_1':faculty,'values_2':courses})
    # {'values_1':faculty,'values_2':courses}

def submit_func(request):
    branch = request.GET.get('branch')
    section = request.GET.get('section')
    semester = request.GET.get('semester')
    subject = request.GET.get('subject')
    faculty = request.GET.get('faculty')

    check_if = sub_fac_relation.objects.only('id').filter(branch_id_id = branch,section_id = section,semester_id = semester,subject_id = subject,id = faculty)
    if not check_if.exists():
        insert = sub_fac_relation.objects.create(branch_id_id = branch,section_id= section,semester_id = semester,subject_id = subject,faculty_id = faculty)
        insert.save()
        print('success')
    else:
        print('something went wrong')
    return "success"



@api_view(['GET'])
def get_info_back(request):
    if(request.GET.get('action') == 'get_fac_relation'):
        branch = request.GET.get('branch')
        semester_get = request.GET.get('semester')
        section = request.GET.get('section')
        print(branch,semester_get,section)
        tasks = sub_fac_relation.objects.filter(branch_id_id = branch,section_id = section,semester_id = semester_get)
        print(tasks)
        serialize = fac_relationSerializer(tasks,many = True)
        return Response(serialize.data)  

@api_view(['GET'])
def check(request):
    query = faculty_table.objects.all()
    serialize = facultySerializer(query,many = True)
    return Response(serialize.data)
