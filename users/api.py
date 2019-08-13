from tastypie.authentication import ApikeyAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import bundle, fields
from functools import partial

from users.models import Teacher, HeadofDepartment, ClassCoordinator



class TeacherResource(ModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        resource_name = 'teacher'
        include_resource_uri = False
        allowed_methods = ['get', 'put']
        always_return_data = True
        limit = 0
        max_limit = 0
        excludes = ['time_created', 'time_modified',
					'user_created', 'user_modified']
        authorization = Authorization()
        authentication = ApikeyAuthentication()
        allowed_update_fields = ['notification_token']

class HoDResource(ModelResource):
    class Meta:
        queryset = HeadofDepartment.objects.all()
        resource_name = 'headofdepartment'
        include_resource_uri = False
        allowed_methods = ['get', 'put']
        always_return_data = True
        limit = 0
        max_limit = 0
        excludes = ['time_created', 'time_modified',
					'user_created', 'user_modified']
        authorization = Authorization()
        authentication = ApikeyAuthentication()
        allowed_update_fields = ['notification_token']

class ClassCoordiantorResource(ModelResource):
    class Meta:
        queryset = ClassCoordinator.objects.all()
        resource_name = 'classcoordinator'
        include_resource_uri = False
        allowed_methods = ['get', 'put']
        always_return_data = True
        limit = 0
        max_limit = 0
        excludes = ['time_created', 'time_modified',
					'user_created', 'user_modified']
        authorization = Authorization()
        authentication = ApikeyAuthentication()
        allowed_update_fields = ['notification_token']