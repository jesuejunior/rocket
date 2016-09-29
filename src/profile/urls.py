# encoding: utf-8
from django.conf.urls import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^users/login', obtain_jwt_token),
]
