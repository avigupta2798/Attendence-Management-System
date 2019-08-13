from django.conf import settings
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from tastypie.api import Api
from django.urls import path

from users.admin import user_admin

from users.views import teacher_login, hod_login, class_coordinator_login

api = Api(api_name = "v1")

urlpatterns = [
                url(r'^api/', include(api.urls)),
                url(r'^admin/', user_admin),
                url(r'^teacher_login/', teacher_login),
                url(r'^hod_login/', hod_login),
                url(r'^class_coordiator_login',class_coordinator_login)
                ]