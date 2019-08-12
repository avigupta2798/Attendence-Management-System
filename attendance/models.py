from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_delete

import re

class AttendanceModel(models.Model):
    user_created = models.ForeignKey(
        User, related_name="%(app_label)s_%(class)s_created", editable=False, null=True, blank=True)
    time_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    user_modified = models.ForeignKey(
        User, related_name="%(app_label)s_%(class)s_related_modified", editable=False, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Semester(AttendanceModel):
    id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=50)
    is_visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.country_name

    class Meta:
        unique_together = ("country_name",)
    
class Department(AttendanceModel):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    semester = models.ForeignKey(Semester)
    is_visible = models.BooleanField(default=True)

    def __unicode__(self):
        return self.state_name_en

    class Meta:
        unique_together = ("state_name", "country")

class Class(AttendanceModel):

    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department)
    semester = models.ForeignKey(Semester,related_name='semester_class', null=True, blank=True, default=None)
    is_visible = models.BooleanField(default=True)
    notation = models.CharField(max_length=10, null=True, blank=True, default=None)

    def __unicode__(self):
        return "%s (%s)" % (self.class_name, self.department.department_name)

    class Meta:
        unique_together = ("village_name", "block")


class Student(AttendanceModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)  # M/F
    phone = models.CharField(max_length=13)
    student_assigned_class = models.ForeignKey(Class, related_name='class_class')
    timestamp = models.CharField(max_length=25, null=True, blank=True)
    image_path = models.CharField(
        max_length=500, default=None, null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    onboarding_incentive_loopsathi=models.ForeignKey('users.PickupAgent',null=True,blank=True)
    onboarding_incentive_date=models.DateField(default=None,null=True,auto_now=False)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.student_assigned_class.class_name)

    class Meta:
        unique_together = ("phone", "name", "student_assigned_class")

