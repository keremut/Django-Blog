from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('full_name','phone','email',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title',)

    def has_add_permission(self,request,obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return False
    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title',)
