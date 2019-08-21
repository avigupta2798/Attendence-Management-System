from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from attendance.models import Department, Student, Class
# Register your models here.

class UsersAdmin(AdminSite):
    def has_permission(self, request):
        return request.user.is_active

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'department_name',]
    list_filter = ['department_name',]
    list_display  = ['id', 'department_name',]
    list_editable = []

class ClassAdmin(admin.ModelAdmin):
    search_fields = ['id', 'class_name', 'semester', 'department__department_name',]
    list_filter = ['class_name', ]
    list_display = ('id', 'class_name', 'semester', 'department',)
    list_editable = []


user_admin = UsersAdmin(name="user_admin")
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Class, ClassAdmin)