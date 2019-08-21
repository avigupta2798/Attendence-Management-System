from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from users.models import Teacher, ClassCoordinator, HeadofDepartment, Log
# Register your models here.

class UsersAdmin(AdminSite):
    def has_permission(self, request):
        return request.user.is_active

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'class_assigned__class_name', 'class_assigned__department__department_name',]
    list_filter = ['class_assigned__class_name', 'class_assigned__department__department_name']
    list_display = ('id', '__user__', 'name',
                    'phone', 'class_assigned', 'user_settings', 'is_active','edit_buffer_days')
    list_editable = ['is_active','edit_buffer_days']  

class HoDAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'department__department_name',]
    list_filter = ['department__department_name',]
    list_display = ('id', '__user__', 'name',
                    'phone', 'department', 'user_settings', 'is_active','edit_buffer_days')
    list_editable = ['is_active','edit_buffer_days']

class ClassCoordinatorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'assigned_class__class_name', 'assigned_class__department__department_name',]
    list_filter = ['assigned_class__class_name', ]
    list_display = ('id', '__user__', 'name', 'phone', 'assigned_class', 'user_settings', 'is_active', 'edit_buffer_days')
    list_editable = ['is_active', 'edit_buffer_days']


user_admin = UsersAdmin(name="user_admin")
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(HeadofDepartment, HoDAdmin)
admin.site.register(ClassCoordinator, ClassCoordinatorAdmin)