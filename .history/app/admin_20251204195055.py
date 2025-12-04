from django.contrib import admin
from app.models import GeneralInfo, Service

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    # to display columns of the table
    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
    ]

    # # to disable permission to add data 
    # def has_add_permission(self, request, obj=None):
    #     return False 

    # # to disable permission to update data 
    # def has_change_permission(self, request, obj=None):
    #     return False 

    # # to disable permission to delete data 
    # def has_delete_permission(self, request, obj=None):
    #     return False ``

    # customize which column/label doesn't has the permission to be edited 
    # selected labels will be non-editable in the admin panel and placed last 
    readonly_fields = [
        'email',
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass