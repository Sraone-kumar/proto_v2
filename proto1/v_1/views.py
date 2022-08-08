from calendar import weekday
from http.client import HTTPResponse
from django.db.models.fields import NullBooleanField
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from numpy import number
from .models import Block_table, Branch_table, Editors, Room_table, Timings_table, Week_table, class_time_table, department_table, faculty_table, lab_information_table, section_table, semester_table, subjects_table, lab_time_table
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer_v_1 import ClassTableSerializer, LabTableSerializer


# Create your views here.


# def index(request):
#     if request.is_ajax():
#         return sumbit_info(request)
#     return render(request,'index.html')

# i know you guys are laughing seeing the typo sumbit instead of submit butwhat should i do realised the typo at the end of project |-\/-|
def sumbit_info(request):

    if request.method == "GET" and request.GET.get('action') == 'get_additional_lab':
        lis = get_additional_lab(request)
        return JsonResponse({'values': lis})

    if request.method == "GET" and request.GET.get('action') == 'get_additional_faculty':
        lis = get_additional_faculty(request)
        return JsonResponse({'values': lis})

    if request.method == "GET" and request.GET.get('action') == 'display_fac_table':
        lis = Get_table_values(request)
        return JsonResponse({'values': lis})

    if request.method == "GET" and request.GET.get('action') == 'insert':
        insert_into_class_time_table(request)
        return JsonResponse({"insertion": "successfull"})

    if request.method == "GET" and request.GET.get('action') == 'insert_lab':
        insert_into_lab_time_table(request)
        return JsonResponse({"insertion": "successfull"})

    if request.method == "GET" and request.GET.get('action') == 'scroll_list':
       # print("it is here")
        val = list(generate_scroll_list(request))
        return JsonResponse({"values": val})

    if request.method == "GET" and request.GET.get('action') == 'faculty_and_subject':
        lis = generate_faculty_and_subjects(request)
        return JsonResponse({"subjects": lis[0], "faculty": lis[1]})

    if request.method == "GET" and request.GET.get('action') == 'lab_and_subject':
        lis = generate_lab(request)
        return JsonResponse({"values": lis})

    if request.method == "GET" and request.GET.get('action') == 'scroll_list_branch':
        lis = generate_branch_scroll_list()
        return JsonResponse({"values": lis})

    if request.method == "GET" and request.GET.get('action') == 'scroll_list_block':
        lis = generate_block_scroll_list()
        return JsonResponse({"values": lis})

    if request.method == "GET" and request.GET.get('action') == 'scroll_list_room':
        lis = generate_room_scroll_list(request.GET.get('block_id'))
        return JsonResponse({"values": lis})
    if request.method == "GET" and request.GET.get('action') == 'scroll_list_semester':
        lis = generate_semester_scroll_list()
        return JsonResponse({"values": lis})
    if request.method == "GET" and request.GET.get('action') == 'scroll_list_section':
        lis = generate_section_scroll_list()
        return JsonResponse({"values": lis})
    return JsonResponse({"timings": "something"})


# .......................faculty and subjects and lab generation....................................
def generate_faculty_and_subjects(request):
    dep_id = int(request.GET.get('department_id'))
    subjects = list(subjects_table.objects.filter(
        department_id=dep_id).values())
    faculty = list(faculty_table.objects.filter(Department_id=dep_id).values())
    # print(subjects)
    # print(faculty)
    return [subjects, faculty]


def generate_lab(request):
    dep_id = int(request.GET.get('department_id'))
    labs = lab_information_table.objects.filter(
        lab_department_id=dep_id).values('lab_id', 'lab_name')
    return list(labs)
# -------------scroll functions............................................................................


def get_additional_faculty(request):
    branch = request.GET.get('branch')
    print('branch: '+branch)
    department_id = Branch_table.objects.filter(
        branch_id=branch).values('department_id')
    fac_query = faculty_table.objects.filter(
        Department_id_id=department_id[0].get('department_id'),).values()
    print('department: ', type(department_id[0].get('department_id')))
    print(fac_query)
    return list(fac_query)


def get_additional_lab(request):
    branch = request.GET.get('branch')
    print('branch: '+branch)
    department_id = Branch_table.objects.filter(
        branch_id=branch).values('department_id')
    lab_query = lab_information_table.objects.filter(
        lab_department=department_id[0].get('department_id'),).values()
    print('department: ', type(department_id[0].get('department_id')))
    # print(fac_query)
    return list(lab_query)


def generate_semester_scroll_list():
    return list(semester_table.objects.all().values())


def generate_section_scroll_list():
    return list(section_table.objects.all().values())


def generate_branch_scroll_list():
    return list(Branch_table.objects.all().values())


def generate_block_scroll_list():
    return list(Block_table.objects.all().values())


def generate_room_scroll_list(id):
    # print(id)
    # print(list(Room_table.objects.filter(block_id_id = int(id)).values()))

    return list(Room_table.objects.filter(block_id_id=id).values())


def generate_scroll_list(request):
    values = department_table.objects.all().values()
    # print(values)
    return values


def Get_table_values(request):
    query = class_time_table.objects.filter(
        faculty_id_id=request.GET.get('faculty')).values()
    print(query)
    return list(query)

# _____________________________________________________________

# ..............................time_table_insertion..................................................


def insert_into_class_time_table(request):

    number_of_inserts = request.GET.get('number_of_inserts')
    subject = request.GET.get('subject')
    faculty = request.GET.get('faculty')
    print('faculty ', faculty)
    fac_query = faculty_table.objects.filter(id=faculty)
    counter = 1 + list(fac_query.values('No_hrs_per_week')
                       )[0].get('No_hrs_per_week')

    block = request.GET.get('block')
    room = request.GET.get('room')
  # compulsary for queriying...below values.......
    weekday = request.GET.get('day')
    branch = request.GET.get('branch')
    section = request.GET.get('section')
    semester = request.GET.get('semester')
    timing = request.GET.get('timing')
    batch = request.GET.get('batch')
    classtype = request.GET.get('class')
    # print('number_of_inserts', type(number_of_inserts))
    if(int(number_of_inserts) == 2):
        faculty_1 = request.GET.get('faculty_1')
        subject_1 = request.GET.get('subject_1')
        batch_1 = request.GET.get('batch_1')
        classtype_1 = request.GET.get('class_1')
        block_1 = request.GET.get('block_1')

        fac_query_1 = faculty_table.objects.filter(id=faculty_1)
        counter_1 = 1 + list(fac_query.values('No_hrs_per_week')
                             )[0].get('No_hrs_per_week')
        print("number_of_inserts:", number_of_inserts)

        room_1 = request.GET.get('room_1')
        print("subject: {},faculty: {} ,weekday: {} , block: {}, room: {},branch: {}, section: {}, semester: {}, timing:{}, batch:{}, classtype:{}".format(
            subject_1, faculty_1, weekday, block, room, branch, section, semester, timing, batch_1, classtype_1))
        no_of_classes = list(class_time_table.objects.filter(
            branch=branch, section=section, semester=semester, weekday_id_id=weekday, timing_id_id=timing))

        print("no_of_classes: ", len(no_of_classes))
        if(len(no_of_classes) == 0):
            print("it is here in number of classes")
            fac_query.update(No_hrs_per_week=counter)
            fac_query_1.update(No_hrs_per_week=counter_1)

            # fac_hrs_update.save()
            insert_query = class_time_table.objects.create(subject_id_id=subject, faculty_id_id=faculty, weekday_id_id=weekday,
                                                           timing_id_id=timing, Room_with_block_id=room, branch_id=branch, section_id=section, semester_id=semester, batch=batch, class_type=classtype)
            # fac_hrs_update.save()
            insert_query_1 = class_time_table.objects.create(subject_id_id=subject_1, faculty_id_id=faculty_1, weekday_id_id=weekday,
                                                             timing_id_id=timing, Room_with_block_id=room_1, branch_id=branch, section_id=section, semester_id=semester, batch=batch_1, class_type=classtype_1)
        elif(len(no_of_classes) == 1):
            print("it is here in no_of_classes ==1")
            check_if_query = class_time_table.objects.only('id').filter(
                branch=branch, section=section, semester=semester, weekday_id=weekday, timing_id=timing)
            print(check_if_query.values())
            if not check_if_query.exists():
                print("damn it is here bro")
                fac_query.update(No_hrs_per_week=counter)
                # fac_hrs_update.save()
                insert_query = class_time_table.objects.create(subject_id_id=subject, faculty_id_id=faculty, weekday_id_id=weekday,
                                                               timing_id_id=timing, Room_with_block_id=room, branch_id=branch, section_id=section, semester_id=semester, batch=batch, class_type=classtype)
            else:
                print("now it is here bla bla bla")
                if check_if_query.values('faculty_id')[0].get('faculty_id') != None:
                    prevFac_id = class_time_table.objects.filter(
                        branch=branch, section=section, semester=semester).values('faculty_id')
                    prevFac = faculty_table.objects.filter(
                        id=list(prevFac_id)[0].get('faculty_id'))
                    prevFac_count = list(prevFac.values('No_hrs_per_week'))[
                        0].get('No_hrs_per_week')
                    if list(fac_query.values('id'))[0].get('id') != prevFac_id:
                        prevFac_count -= 1
                        counter -= 1
                        prevFac.update(No_hrs_per_week=prevFac_count)
            # counter -= 1

            fac_query.update(No_hrs_per_week=counter)
            class_time_table.objects.filter(id=check_if_query.values()[0]['id']).update(
                subject_id_id=subject, faculty_id_id=faculty, room_with_block=room, batch=batch, class_type=classtype)

            fac_query_1.update(No_hrs_per_week=counter_1)
            insert_query_1 = class_time_table.objects.create(subject_id_id=subject_1, faculty_id_id=faculty_1, weekday_id_id=weekday,
                                                             timing_id_id=timing, Room_with_block_id=room_1, branch_id=branch, section_id=section, semester_id=semester, batch=batch_1, class_type=classtype_1)

        else:
            print("it is here in no_of_classes ==2")
            check_if_query = class_time_table.objects.only('id').filter(
                branch=branch, section=section, semester=semester, weekday_id=weekday, timing_id=timing)
            print(check_if_query.values())

            if not check_if_query.exists():
                print("damn it is here bro")
                fac_query.update(No_hrs_per_week=counter)
                # fac_hrs_update.save()
                insert_query = class_time_table.objects.create(subject_id_id=subject, faculty_id_id=faculty, weekday_id_id=weekday,
                                                               timing_id_id=timing, Room_with_block_id=room, branch_id=branch, section_id=section, semester_id=semester, batch=batch, class_type=classtype)
            else:
                print("now it is here bla bla bla")
                # if check_if_query.values('faculty_id')[0].get('faculty_id') != None:
                #     prevFac_id = class_time_table.objects.filter(
                #         branch=branch, section=section, semester=semester).values('faculty_id')
                #     prevFac = faculty_table.objects.filter(
                #         id=list(prevFac_id)[0].get('faculty_id'))
                #     prevFac_1 = faculty_table.objects.filter(
                #         id=list(prevFac_id)[1].get('faculty_id'))
                #     prevFac_count = list(prevFac.values('No_hrs_per_week'))[
                #         0].get('No_hrs_per_week')
                #     prevFac_count_1 = list(prevFac_1.values('No_hrs_per_week'))[
                #         0].get('No_hrs_per_week')
                #     if list(fac_query.values('id'))[0].get('id') != prevFac_id:
                #         prevFac_count -= 1
                #         counter -= 1
                #         prevFac.update(No_hrs_per_week=prevFac_count)

            class_time_table.objects.filter(id=check_if_query.values()[0]['id']).update(
                subject_id_id=subject, faculty_id_id=faculty, Room_with_block=room, batch=batch, class_type=classtype)
            class_time_table.objects.filter(id=check_if_query.values()[1]['id']).update(
                subject_id_id=subject_1, faculty_id_id=faculty_1, Room_with_block=room_1, batch=batch_1, class_type=classtype_1)

    else:

        print("subject: {},faculty: {} ,weekday: {} , block: {}, room: {},branch: {}, section: {}, semester: {}, timing:{}, batch:{}, classtype:{}".format(
            subject, faculty, weekday, block, room, branch, section, semester, timing, batch, classtype))

        check_if_query = class_time_table.objects.only('id').filter(
            branch=branch, section=section, semester=semester, weekday_id=weekday, timing_id=timing)
        print(check_if_query.values())
        if not check_if_query.exists():
            print("damn it is here bro")
            fac_query.update(No_hrs_per_week=counter)
            # fac_hrs_update.save()
            insert_query = class_time_table.objects.create(subject_id_id=subject, faculty_id_id=faculty, weekday_id_id=weekday,
                                                           timing_id_id=timing, Room_with_block_id=room, branch_id=branch, section_id=section, semester_id=semester, batch=batch, class_type=classtype)
        else:
            print("now it is here bla bla bla")
            if check_if_query.values('faculty_id')[0].get('faculty_id') != None:
                prevFac_id = class_time_table.objects.filter(
                    branch=branch, section=section, semester=semester).values('faculty_id')
                prevFac = faculty_table.objects.filter(
                    id=list(prevFac_id)[0].get('faculty_id'))
                prevFac_count = list(prevFac.values('No_hrs_per_week'))[
                    0].get('No_hrs_per_week')
                if list(fac_query.values('id'))[0].get('id') != prevFac_id:
                    prevFac_count -= 1
                    counter -= 1
                    prevFac.update(No_hrs_per_week=prevFac_count)
            # counter -= 1

            fac_query.update(No_hrs_per_week=counter)
            class_time_table.objects.filter(id=check_if_query.values()[0]['id']).update(
                subject_id_id=subject, faculty_id_id=faculty, Room_with_block=room, batch=batch, class_type=classtype)

    return "success"


def insert_into_lab_time_table(request):

    lab = request.GET.get('lab')
    no_of_hours = request.GET.get('no_of_hours')
    subject = request.GET.get('subject')
    faculty = request.GET.get('faculty')

    # block = request.GET.get('block')
    # room = request.GET.get('room')
  # compulsary for queriying...below values.......
    weekday = request.GET.get('day')
    branch = request.GET.get('branch')
    section = request.GET.get('section')
    semester = request.GET.get('semester')
    timing = request.GET.get('timing')
    time_1 = request.GET.get('time_1')
    time_2 = request.GET.get('time_2')
    extra_faculty = request.GET.get('extra_faculty')
    print("hererrrrrr")
    fac_name = faculty_table.objects.filter(
        id=extra_faculty).values()
    print(fac_name)
    print("its here in the lab bro")
    print("lab:{},no_of_hours:{},subject: {},faculty: {} ,weekday: {},branch: {}, section: {}, semester: {}, timing:{},time_1:{},time_2:{},extra_fac:{}".format(
        lab, no_of_hours, subject, faculty, weekday, branch, section, semester, timing, time_1, time_2, extra_faculty))

    check_if_query = lab_time_table.objects.only('id').filter(
        branch=branch, section=section, semester=semester, week=weekday, time=timing)
    if not check_if_query.exists():
        insert_query = lab_time_table.objects.create(lab_id=lab, lab_course_id=subject, lab_faculty_id=faculty, week_id=weekday,
                                                     time_id=timing, branch_id=branch, section_id=section, semester_id=semester, no_of_hours=no_of_hours, time_1=time_1, time_2=time_2, extra_faculty=extra_faculty)
        insert_query.save()
    else:
        lab_time_table.objects.filter(id=check_if_query.values()[0]['id']).update(
            lab_id=lab, lab_course_id=subject, lab_faculty_id=faculty, time_1=time_1, time_2=time_2, extra_faculty=extra_faculty)

    return "success lab"


def delete(request):
    branch = request.GET.get('branch')
    section = request.GET.get('section')
    semester = request.GET.get('semester')
    time = request.GET.get('time')
    week = request.GET.get('week')
    print(branch, section, semester, time, week)
    if request.GET.get('action') == "delete_class":

        queryDelete = class_time_table.objects.filter(
            branch=branch, section=section, semester=semester, timing_id_id=time, weekday_id_id=week)
        print(queryDelete)
        if queryDelete.exists():
            fac_id = queryDelete.values('faculty_id')
            # print(fac_id)
            updateCount = faculty_table.objects.filter(
                id=fac_id[0].get('faculty_id'))
            # print(updateCount.values('id','faculty_id','faculty_name'))
            updateCount.update(No_hrs_per_week=abs(
                1-updateCount.values('No_hrs_per_week')[0].get('No_hrs_per_week')))
            # print(fac_id)

            # delete at last otherwise values will change..
            queryDelete.update(subject_id_id=None,
                               faculty_id_id=None, batch=None, class_type=None)

        # updateCount = faculty_table.objects.filter(id = class_time_table.objects.filter(branch = branch,section = section,semester = semester,timing_id_id = time,weekday_id_id = week ).values('faculty_id')[0].get('faculty_id'))
    elif request.GET.get('action') == "delete_lab":
        queryDelete = lab_time_table.objects.filter(branch=branch, section=section, semester=semester, time_id=time, week_id=week).update(
            lab_id=None, lab_course_id=None, lab_faculty_id=None)

    # print(list(queryDelete))

    return JsonResponse({"task": "success"})

# main_page....!!!!


def HomePage(request):
    return render(request, 'HomePage.html')


def testCheck(request):
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    # print(timings)
    val = {"timings": timings, "days": days}
    # print(timings)
    if request.is_ajax:
        return sumbit_info(request)
    return render(request, 'testCheck.html', val)


def editor_v2(request):
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    # print(timings)
    val = {"timings": timings, "days": days}
    return render(request, 'editor_v2.html', val)


def lab_editor(request):

    if 'user' not in request.session:
        print("session is not set in editor")
        # redirect here
        # return redirect('login')
    # print("session assined",request.session['user'])
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    # print(timings)
    val = {"timings": timings, "days": days}
    return render(request, 'lab_editor.html', val)


def student_display(request):
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    # print(timings)
    val = {"timings": timings, "days": days}
    return render(request, 'student.html', val)


def lab_display(request):
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    val = {"timings": timings, "days": days}
    return render(request, 'lab_display.html', val)


def display_tables(request):
    if 'user' not in request.session:
        print("session not set in display")
        # return redirect('login')
    timings = Timings_table.objects.all().values()
    days = Week_table.objects.all().values()
    val = {"timings": timings, "days": days}
    # if request.is_ajax():
    #     return sumbit_info(request)
    return render(request, 'display.html', val)


def testing(request):
    if request.is_ajax():
        query = list(class_time_table.objects.filter(
            faculty_id_id=request.GET.get('faculty_id')).values())
        print(query)
        return JsonResponse({'data': query})
    return render(request, 'testing_serialization.html')


@api_view(['GET'])
def check_view(request):
    print(request.GET.get('faculty'))
    tasks = class_time_table.objects.filter(
        faculty_id_id=request.GET.get('faculty'))
    print(tasks)
    labs = lab_time_table.objects.filter(
        lab_faculty=request.GET.get('faculty'))
    serialize = ClassTableSerializer(tasks, many=True)
    serialize_2 = LabTableSerializer(labs, many=True)
    return Response({'class': serialize.data, 'lab': serialize_2.data})


def styling_check(request):
    return render(request, 'styling_check.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        print(uname)
        pwd = request.POST.get('password')
        if uname == 'admin' and pwd == "123456":
            return redirect('Home_page')
        if uname:
            user = list(faculty_table.objects.filter(
                faculty_name=uname).values('id'))
            print(user[0].get('id'))
            check_user = Editors.objects.filter(
                user=user[0].get('id'), password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('lab_editor')
        else:
            return HTTPResponse('Please enter valid username')

    return render(request, 'Login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
