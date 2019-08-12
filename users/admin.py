from django.contrib import admin
from django.contrib.admin.sites import AdminSite

from users.models import Teacher, ClassCoordinator, HeadofDepartment, Log
# Register your models here.

class UsersAdmin(AdminSite):
    def has_permission(self, request):
        return request.user.is_active

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'class_assigned__class_name', 'class_assigned__department__department_name', 'class_assigned__semester__semester_name',]
    list_filter = ['class_assigned__class_name', 'class_assigned__department__department_name']
    list_display = ('id', '__user__', 'name',
                    'phone', 'class_assigned', 'user_settings', 'is_active','edit_buffer_days')
    list_editable = ['is_active','edit_buffer_days']  


user_admin = UsersAdmin(name="user_admin")
user_admin.register(Teacher, TeacherAdmin)