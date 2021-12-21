from django.db.models import manager
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer_v_1 import BranchSerializer, ClassTableSerializer, SubjectsSerializer, fac_relationSerializer, facultySerializer

from .sub_fac_model import sub_fac_relation

from .models import Branch_table, Timings_table, Week_table, class_time_table, faculty_table, lab_information_table, subjects_table

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
        classquery = class_time_table.objects.filter(branch_id = branch,section = section,semester= semester_get)
        department_id = list(Branch_table.objects.filter(branch_id=branch).values('department_id'))
        print("department_id:",department_id[0]['department_id'])
        labQuery = list(lab_information_table.objects.filter(lab_department_id = department_id[0]['department_id'] ).values('lab_id','lab_name'))
        print("lab_query: ",labQuery)
        print(tasks)
        print(classquery)
        serialize = fac_relationSerializer(tasks,many = True)
        serialize_class = ClassTableSerializer(classquery,many = True)
        return Response({'sub_fac':serialize.data,'class':serialize_class.data,'lab':labQuery})  


@api_view(['GET'])
def check(request):
    query = faculty_table.objects.all()
    serialize = facultySerializer(query,many = True)
    return Response(serialize.data)


def total_script(request):
    time = list(Timings_table.objects.all().values());
    weekdays = list(Week_table.objects.all().values());
    return render(request,'total_script.html',{'time':time,'week':weekdays})


@api_view(['GET'])
def runer(request):
    query = Branch_table.objects.all()
    subjects = subjects_table.objects.all()
    serialize_1 = BranchSerializer(query,many = True)
    serialize_2 = SubjectsSerializer(subjects,many=True)
    return Response({'branch':serialize_1.data,'faculty':serialize_2.data})

