from django.contrib import admin
from .models import lab_information_table, lab_time_table, subjects_table,Designation_table,department_table, faculty_table, class_time_table,Timings_table,Block_table,Week_table,Room_table,Branch_table,semester_table,section_table
from .sub_fac_model import sub_fac_relation
from .resources import FacultyResource, SubjectResource
from django.urls import path
from django.shortcuts import render
from django import forms
from tablib import Dataset
import pandas as pd
import numpy as np

class CSVImportFormfac(forms.Form):
    csv_upload_fac=forms.FileField()
class CSVImportFormsub(forms.Form):
    csv_upload_sub=forms.FileField()



class subAdmin(admin.ModelAdmin):
    # list_display = ('subject_name','semester_taught','department_id')
    list_display=('subject_id','subject_code','subject_name','subject_credits','Elective_type','semester_taught','department_id')
    search_fields=['subject_name']
    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csvsub/',self.upload_csvsub),]
        return new_urls+urls
    def upload_csvsub(self,request):
        if request.method=="POST":
            subject_resource = SubjectResource()
            dataset = Dataset()
            new_subject=request.FILES['csv_upload_sub']
            imported_data2=dataset.load(new_subject.read(),format="xlsx")
            dfsubject=pd.read_excel(new_subject)
            semester_list = semester_table.objects.all()
            sem_id=[]
            sem_number=[]
            for sem in semester_list:
                x=sem.semester_id
                y=sem.semester_number
                sem_id.append(x)
                sem_number.append(y)
            d = {'semester_id':sem_id,'semester_number':sem_number}
            dfsemester= pd.DataFrame(d)
            for length1 in dfsemester.semester_number:
                for len2 in dfsubject.semester_taught:
                    variable=(length1==len2)
                    if variable==True:
                        indexx=dfsemester.semester_number[dfsemester.semester_number == length1].index[0]
                        dfsubject.semester_taught.replace(to_replace=len2,value=dfsemester.semester_id[indexx],inplace=True)
            # for data in dffaculty: 
            for i,row in dfsubject.iterrows():   
                col1=row[0]
                col2=row[1]
                col3=row[2]
                col4=row[3]
                col5=row[4]
                col6=row[5]
                col7=row[6]
                data1=(col1,col2,col3,col4,col5,col6,col7)
                value4=subjects_table(
                    data1[0],
                    data1[1],
                    data1[2],
                    data1[3],
                    data1[4],
                    data1[5],
                    data1[6]
                )
                value4.save()
        print("hello")
        form=CSVImportFormsub()
        data1 = {"form":form}
        return render(request,"admin/csv_upload.html",data1)

class classAdmin(admin.ModelAdmin):
    list_display = ('subject_id','faculty_id','branch','section','semester','Room_with_block')
    

class facAdmin(admin.ModelAdmin):
    list_display=('id','faculty_id','faculty_name','No_hrs_per_week','Designation_id','Department_id') 
    search_fields=['faculty_name']
    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csvfac/',self.upload_csvfac),]
        return new_urls+urls
    
    def upload_csvfac(self,request):
        if request.method=="POST":
            faculty_resource = FacultyResource()
            dataset = Dataset()
            new_faculty=request.FILES['csv_upload_fac']
            imported_data1=dataset.load(new_faculty.read(),format="xlsx")
            dffaculty=pd.read_excel(new_faculty)
            department_list = department_table.objects.all()
            dep_id=[]
            dep_name=[]
            for dep in department_list:
                x=dep.department_id
                y=dep.department_name
                dep_id.append(x)
                dep_name.append(y)
            d = {'department_id':dep_id,'department_name':dep_name}
            dfdepart = pd.DataFrame(d)
            designation_list = Designation_table.objects.all()
            des_id=[]
            des_name=[]
            for des in designation_list:
                x=des.designation_id
                y=des.designation_name
                des_id.append(x)
                des_name.append(y)
            d1 = {'designation_id':des_id,'designation_name':des_name}
            dfdesign= pd.DataFrame(d1)
            for length in dfdesign.designation_name:
                for len1 in dffaculty.designation_id:
                    variable=(length==len1)
                    if variable==True:
                        indexx=dfdesign.designation_name[dfdesign.designation_name == length].index[0]
                        dffaculty.designation_id.replace(to_replace=len1,value=dfdesign.designation_id[indexx],inplace=True)

            for length1 in dfdepart.department_name:
                for len2 in dffaculty.department_id:
                    variable=(length1==len2)
                    if variable==True:
                        index1=dfdepart.department_name[dfdepart.department_name == length1].index[0]
                        dffaculty.department_id.replace(to_replace=len2,value=dfdepart.department_id[index1],inplace=True)
            # for data in dffaculty: 
            for i,row in dffaculty.iterrows():    
                col1=row[0]
                col2=row[1]
                col3=row[2]
                col4=row[3]
                col5=row[4]
                col6=row[5]
                data=(col1,col2,col3,col4,col5,col6)
                value1=faculty_table(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5]
                )
                value1.save()
        form=CSVImportFormfac()
        data = {"form":form}
        return render(request,"admin/csv_upload.html",data)



admin.site.register(subjects_table,subAdmin)
admin.site.register(Designation_table)
admin.site.register(department_table)
admin.site.register(faculty_table,facAdmin)
admin.site.register(class_time_table,classAdmin)
admin.site.register(Timings_table)
admin.site.register(Block_table)
admin.site.register(Week_table)
admin.site.register(Room_table)
admin.site.register(Branch_table)
admin.site.register(section_table)
admin.site.register(semester_table)
admin.site.register(sub_fac_relation)
admin.site.register(lab_information_table)
admin.site.register(lab_time_table)
# Register your models here.
