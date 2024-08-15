from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fields = ("name", "age", "father_name",)
admin.site.register(Student, StudentAdmin)
admin.site.register(Category)
admin.site.register(Book)

class AdmitionAdmin(admin.ModelAdmin):
    list_display = ("name","father_name","dob","email","phone","address")
admin.site.register(Admition,AdmitionAdmin)
