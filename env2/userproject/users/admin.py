from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Sector)

class WorkerAdmin(admin.ModelAdmin):
    list_disply =("sector", "AWC_Code","AWC_Name","AWW_Name") 
admin.site.register(Worker,WorkerAdmin)