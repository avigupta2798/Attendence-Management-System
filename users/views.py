import os
from PIL import Image, ImageDraw, ImageFont
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.
from users.models import Teacher, Log
from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseNotAllowed, \
    HttpResponseForbidden
from django.apps import apps
from tastypie.models import ApiKey, create_api_key
import datetime
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from rest_framework.response import Response
from rest_framework import status
import json
import datetime
import random
from rest_framework.authtoken.models import Token
from pygeocoder import Geocoder

def get_latest_timestamp():
    try:
        timestamp = Log.objects.latest('id').timestamp
    except Exception:
        timestamp = datetime.datetime.now()
    return timestamp

def get_auth(request, app_name='users', model_name=None):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        api_key = None
        model_user_obj = None
        if user:
            model_obj = apps.get_model(app_name, model_name)
            model_user_obj = model_obj.objects.filter(user=user, user__is_active=True)
            try:
                api_key = ApiKey.objects.get(user=user)
            except ApiKey.DoesNotExist:
                api_key = ApiKey.objects.create(user=user)
                api_key.save()

        return model_user_obj, api_key

@csrf_exempt
def get_auth_apps(request):
    key = request.POST['access_token']
    users = Token.objects.filter(key=key)
    if users:
        user = users[0].user
        return HttpResponse(json.dumps({'groups': user.groups.values_list('name', flat=True).distinct()}))

@csrf_exempt
def teacher_login(request):
    user, api_key = get_auth(request, model_name='Teacher')

    if user and api_key and user[0].is_active:
        reg_token = None
        version = None
        if 'notification_token' in request.POST and request.POST['notification_token']:
            reg_token = request.POST['notification_token']
            Teacher.objects.filter(notification_token=reg_token).update(notification_token=None)

        if 'version' in request.POST and request.POST['version']:
            version = request.POST['version']
        if reg_token:
            user.update(notification_token=reg_token)
        if version:
            user.update(app_version=version)
        if 'user_settings' in request.POST and request.POST['user_settings']:
            user.update(user_settings=str(request.POST['user_settings']))

        return HttpResponse(json.dumps(
            {
                'key': api_key.key,
                'name': user[0].name,
                'id': user[0].id,
                'user_id': user[0].user_id,
                'user_name': user[0].user.username,
                'phone_number': user[0].phone,
                'notification_token': user[0].notification_token,
                'edit_buffer_days': user[0].edit_buffer_days,
                # Last Login Time
                'timestamp': str(get_latest_timestamp().strftime('%Y-%m-%d %H:%M:%S.%f')),
                'role': user[0].role,
                'semester_id':user[0].class_assigned.department.semester.id
            }
        ))
    else:
        return HttpResponseNotFound("User Does Not Exist")


@csrf_exempt
def hod_login(request):
    user, api_key = get_auth(request, model_name='HeadofDepartment')

    if user and api_key and user[0].is_active:
        reg_token = None
        version = None
        if 'notification_token' in request.POST and request.POST['notification_token']:
            reg_token = request.POST['notification_token']
            Teacher.objects.filter(notification_token=reg_token).update(notification_token=None)

        if 'version' in request.POST and request.POST['version']:
            version = request.POST['version']
        if reg_token:
            user.update(notification_token=reg_token)
        if version:
            user.update(app_version=version)
        if 'user_settings' in request.POST and request.POST['user_settings']:
            user.update(user_settings=str(request.POST['user_settings']))

        return HttpResponse(json.dumps(
            {
                'key': api_key.key,
                'name': user[0].name,
                'id': user[0].id,
                'user_id': user[0].user_id,
                'user_name': user[0].user.username,
                'phone_number': user[0].phone,
                'notification_token': user[0].notification_token,
                'edit_buffer_days': user[0].edit_buffer_days,
                # Last Login Time
                'timestamp': str(get_latest_timestamp().strftime('%Y-%m-%d %H:%M:%S.%f')),
                'role': user[0].role,
                'semester_id':user[0].department.semester.id
            }
        ))
    else:
        return HttpResponseNotFound("User Does Not Exist")

@csrf_exempt
def class_coordinator_login(request):
    user, api_key = get_auth(request, model_name='ClassCoordinator')

    if user and api_key and user[0].is_active:
        reg_token = None
        version = None
        if 'notification_token' in request.POST and request.POST['notification_token']:
            reg_token = request.POST['notification_token']
            Teacher.objects.filter(notification_token=reg_token).update(notification_token=None)

        if 'version' in request.POST and request.POST['version']:
            version = request.POST['version']
        if reg_token:
            user.update(notification_token=reg_token)
        if version:
            user.update(app_version=version)
        if 'user_settings' in request.POST and request.POST['user_settings']:
            user.update(user_settings=str(request.POST['user_settings']))

        return HttpResponse(json.dumps(
            {
                'key': api_key.key,
                'name': user[0].name,
                'id': user[0].id,
                'user_id': user[0].user_id,
                'user_name': user[0].user.username,
                'phone_number': user[0].phone,
                'notification_token': user[0].notification_token,
                'edit_buffer_days': user[0].edit_buffer_days,
                # Last Login Time
                'timestamp': str(get_latest_timestamp().strftime('%Y-%m-%d %H:%M:%S.%f')),
                'role': user[0].role,
                'semester_id':user[0].class_assigned.department.semester.id
            }
        ))
    else:
        return HttpResponseNotFound("User Does Not Exist")

