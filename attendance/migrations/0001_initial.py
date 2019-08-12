# Generated by Django 2.2.4 on 2019-08-12 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
                ('user_created', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_semester_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_semester_related_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('semester_name',)},
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Semester')),
                ('user_created', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_department_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_department_related_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('department_name', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=50)),
                ('is_visible', models.BooleanField(default=True)),
                ('notation', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='attendance.Department')),
                ('semester', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='semester_class', to='attendance.Semester')),
                ('user_created', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_class_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_class_related_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('class_name', 'department')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=13)),
                ('timestamp', models.CharField(blank=True, max_length=25, null=True)),
                ('image_path', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('onboarding_incentive_date', models.DateField(default=None, null=True)),
                ('student_assigned_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_class', to='attendance.Class')),
                ('user_created', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_student_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attendance_student_related_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('phone', 'name', 'student_assigned_class')},
            },
        ),
    ]