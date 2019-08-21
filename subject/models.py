from django.db import models

from django.contrib.auth.models import User
from attendance.models import AttendanceModel, Class, Department
from users.models import Teacher
from django.db.models.signals import post_save, pre_delete
from attendance.models import AttendanceModel
import datetime

# Create your models here.

class Subject(AttendanceModel):

    id = models.AutoField(primary_key=True)
    subject_id = models.CharField(max_length=25, null=True, blank=True)
    subject_code = models.CharField(max_length=25, null=True, blank=True)
    subject_name = models.CharField(max_length=50, null=True, blank=True)
    timestamp = models.CharField(max_length=25, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True, related_name="teacher")
    
    class Meta:
        verbose_name_plural = "Subjects"
        unique_together = ("teacher", "id")

    # def __unicode__(self):
    #     return "%s %s" % (self.booking, self.booking_detail)
