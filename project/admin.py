from django.contrib import admin
from .models import Service, Project, Program
# Register your models here.

class  ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at','created_at')
    prepopulated_fields = {'slug': ('name',)}

class  ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','updated_at','created_at')
    prepopulated_fields = {'slug': ('name',)}

class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon','updated_at','created_at')
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Service, ServiceAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Project, ProjectAdmin)