from import_export import resources
from .models import faculty_table,subjects_table

class FacultyResource(resources.ModelResource):
    class meta:
        model=faculty_table

class SubjectResource(resources.ModelResource):
    class meta:
        model=subjects_table
