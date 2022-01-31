from operator import truediv
from django.db.models import manager
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from v_1 import data_loader

from .serializer_v_1 import BranchSerializer, ClassTableSerializer, LabTableSerializer, SubFacSerializer, SubjectsSerializer, fac_relationSerializer, facultySerializer

from .sub_fac_model import sub_fac_relation

from .models import Branch_table, Timings_table, Week_table, class_time_table, faculty_table, lab_information_table, lab_time_table, subjects_table

def sub_fac(request):
    return render(request,'sub_fac_editor.html')
@api_view(["GET"])
def get_info(request):
    # faculty = []
    if request.GET.get('action') == 'info' or request.GET.get('action') == 'fac_sort_info' :
        branch = request.GET.get('branch')
        semester  = request.GET.get('semester')
        section = request.GET.get('section')
        department = list(Branch_table.objects.filter(branch_id = branch).values('department_id'))
        faculty = list(faculty_table.objects.filter(Department_id_id = department[0].get('department_id')).values('id','faculty_name','No_hrs_per_week'))
        if request.GET.get('action') == 'fac_sort_info':
            return JsonResponse({"values":faculty})
        #There should be condition for 1,2,3 semester subjects--which can be from
        #different departments-
        courses = list(subjects_table.objects.filter(department_id_id = department[0].get('department_id'),semester_taught_id = semester).values('subject_id','subject_name'))
        # print(faculty)
        # print(courses)

        # print(branch,semester,section)
        check_query = sub_fac_relation.objects.filter(branch_id_id = branch,section_id = section,semester_id =semester)

        # print("check_query: ",check_query)
        if check_query.exists():
            sub_fac_serialize = SubFacSerializer(check_query,many = True)
            return Response({"fac_sub":sub_fac_serialize.data,'faculty':faculty})

    if(request.GET.get('action') == 'submit'):
        submit_func(request)
        return JsonResponse({'success':'success'})
    print("its here")
    return JsonResponse({"something happened":"dont know what"})
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
        #print(branch,semester_get,section)
        tasks = sub_fac_relation.objects.filter(branch_id_id = branch,section_id = section,semester_id = semester_get)
        classquery = class_time_table.objects.filter(branch_id = branch,section = section,semester= semester_get)
        department_id = list(Branch_table.objects.filter(branch_id=branch).values('department_id'))
        labTimeTable = lab_time_table.objects.filter(branch_id = branch,semester_id = semester_get,section_id = section)
       #print("department_id:",department_id[0]['department_id'])
        labQuery = list(lab_information_table.objects.filter(lab_department_id = department_id[0]['department_id'] ).values('lab_id','lab_name'))
        #print("lab_query: ",labQuery)
        #print(tasks)
        #print(classquery)
        serialize = fac_relationSerializer(tasks,many = True)
        serialize_class = ClassTableSerializer(classquery,many = True)
        serialize_lab = LabTableSerializer(labTimeTable,many =True)
        return Response({'sub_fac':serialize.data,'class':serialize_class.data,'lab':labQuery,'lab_time_table':serialize_lab.data})  
    if request.GET.get('action') == 'display_lab_info':
        dep = request.GET.get('department')
        lab = request.GET.get('lab')
        get_branch = Branch_table.objects.filter(department_id = dep).values('branch_id')
        query = lab_time_table.objects.filter(branch_id = get_branch[0].get('branch_id'),lab_id = lab)
        seri_lab = LabTableSerializer(query,many = True)
        # print(seri_lab.data)
        return Response({'values':seri_lab.data})

@api_view(['GET'])
def check(request):
    query = faculty_table.objects.all()
    serialize = facultySerializer(query,many = True)
    return Response(serialize.data)


def total_script(request):
    time = list(Timings_table.objects.all().values())
    weekdays = list(Week_table.objects.all().values())
    return render(request,'total_script.html',{'time':time,'week':weekdays})


@api_view(['GET'])
def runer(request):
    # query = Branch_table.objects.all()
    # subjects = subjects_table.objects.all()
    subFac = sub_fac_relation.objects.all()
    # serialize_1 = BranchSerializer(query,many = True)
    # serialize_2 = SubjectsSerializer(subjects,many=True)
    serialize_3 = SubFacSerializer(subFac,many = True)
    return Response({'values':serialize_3.data})

def upload(request):
    return render(request,'upload.html')

def upload_submit(request):
    print(request.GET.get('val'))
    data_loader.loader(request)
    return render(request,'upload.html')


