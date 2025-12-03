from django.contrib import admin
from app.models import GeneralInfo


# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    pass