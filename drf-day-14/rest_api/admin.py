from django.contrib import admin
from . models import Aiquest

# Register your models here.
@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display = ['id','student_name','class_name','seat']