from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from tastypie.api import Api
from django.urls import path
from users import views as users_views
from users.admin import user_admin

from users.views import teacher_login, hod_login, class_coordinator_login

api = Api(api_name = "v1")

urlpatterns = [
                url('api/', include(api.urls)),
                url('teacher_login/',users_views.teacher_login, teacher_login),
                url('admin/',users_views.teacher_login, teacher_login),
                url('hod_login/', users_views.hod_login, hod_login),
                url('class_coordiator_login/', users_views.class_coordinator_login, class_coordinator_login)
                ]