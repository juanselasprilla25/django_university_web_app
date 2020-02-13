from django.contrib import admin
from university_web_app.Apps.Course_Manager.models import *

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)

