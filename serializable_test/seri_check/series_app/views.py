import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DepartmentSerializer
from .models import Department_table
# Create your views here.


def ind_launch(request):
    return render(request,'ind.html')


@api_view(['GET'])
def req(request):
    some_urls = {
        'one' : 'one_two',
        'two' : 'two_three',
    }

    return Response(some_urls)

@api_view(['GET'])
def department_list(request):
    print("id: ",request.GET.get('id'))
    tasks = Department_table.objects.filter(id = request.GET.get('id'))
    print(tasks)
    serializer = DepartmentSerializer(tasks, many=True)
    print(serializer.data)
    return Response(serializer.data)