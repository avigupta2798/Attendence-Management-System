from django.db import models

from django.contrib.auth.models import User
from attendance.models import Class, Department
from subject.constants import TEACHER_USER_ROLE
from django.db.models.signals import post_save, pre_delete
from attendance.models import AttendanceModel
import datetime

# Create your models here.


def user_new_unicode(self):
    return '%s - %s (%s)' % (self.pk, self.get_username(), self.get_full_name())

User.__str__ = user_new_unicode

class BaseUserModel(AttendanceModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    notification_token = models.CharField(
        max_length=300, blank=True, null=True, default="")
    app_version = models.CharField(max_length=10, blank=True, null=True)
    user_settings = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="User Configuration")
    buffer_days = models.IntegerField(default=45)
    edit_buffer_days = models.IntegerField(default=3)
    

    class Meta:
        abstract = True

class Teacher(BaseUserModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="teacher")
    role = models.IntegerField(choices=TEACHER_USER_ROLE, default=1)
    class_assigned = models.ForeignKey(Class, on_delete=models.PROTECT, default=None, null=True)
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __user__(self):
        return "%s" % self.user.username
    
    def __str__(self):
        return "%s" % self.name


class HeadofDepartment(BaseUserModel):
    USER = 1
    TEST = 2
    DEMO = 3


    HOD_USER_ROLE = (
        (USER, "USER"),
        (TEST, "TEST"),
        (DEMO, "DEMO")
    )

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="head_of_department")
    role = models.IntegerField(choices=HOD_USER_ROLE, default=1)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, default=None, null=True)
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    
    def __user__(self):
        return "%s" % self.user.username
    
    def __str__(self):
        return "%s" % self.name


class ClassCoordinator(BaseUserModel):
    USER = 1
    TEST = 2
    DEMO = 3


    COORDINATOR_USER_ROLE = (
        (USER, "USER"),
        (TEST, "TEST"),
        (DEMO, "DEMO")
    )

    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="class_coordinator")
    role = models.IntegerField(choices=COORDINATOR_USER_ROLE, default=1)
    assigned_class = models.ForeignKey(Class, on_delete=models.PROTECT, related_name="coordinator", default=None, null=True)
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __user__(self):
        return "%s" % self.user.username
    
    def __str__(self):
        return "%s" % self.name

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=False, default=datetime.datetime.utcnow)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='log_user')
    user_type = models.CharField(max_length=100)
    action = models.IntegerField()
    entry_table = models.CharField(max_length=100)
    model_id = models.IntegerField(null=True)
