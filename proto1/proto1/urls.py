"""proto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from v_1 import viewForUpload
from v_1 import debugy
from v_1 import views_2
from v_1 import views

urlpatterns = [

    # admin page----------------------------
    path('admin/', admin.site.urls, name='admin'),


    # path('index/', views.index),
    path('get/ajax/submit_info', view=views.sumbit_info, name="submit_info"),
    # path('testCheck/', views.testCheck),
    # path('get/ajax/check',views.some,name='some'),
    # path('test/', views.testing),
    # path('get/ajax/test', views.testing, name='test'),
    path('check_view/', views.check_view, name='check_view'),
    path('styling/', views.styling_check),
    path('editor-2/', views.editor_v2, name='editor_v2'),
    path('get/ajax/get_info', views_2.get_info, name='get_info'),
    path('get/ajax/get_info_back', views_2.get_info_back, name='get_info_back'),
    path('check/', views_2.check),
    # path('upload/',views_2.upload,name = 'upload'),
    # path('upload_submit',views_2.upload_submit,name='upload_submit'),


    ############ pages urls(12-october-2021)..............current_working_versions..............#####################
    # Home Page
    path('Home', views.HomePage, name='Home_page'),
    # editor page
    path('editor_v3/', views.lab_editor, name='lab_editor'),
    # lab information display page
    path('lab_display', views.lab_display, name="lab_display"),
    # student information display page
    path('student/', views.student_display, name='student'),
    # subjects and facutly assignment page
    path('sub_fac/', views_2.sub_fac, name='sub_fac'),
    # facutly information display page
    path('display/', views.display_tables, name='display'),


    # Next_version....testing with updates(12-march-2022)
    path('editor_v4_replica', views_2.total_script, name='editor_v4_prototype'),





    # login and logout......
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),

    # upload functionality url....
    path('uploader/', viewForUpload.uploadBasic, name="uploader"),

    # testing urls.......
    path('goo/', debugy.check_fac),
    path('runer/', views_2.runer),
]
