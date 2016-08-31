# encoding: utf-8
from django.conf.urls import *

from profile.resources.user import User

urlpatterns = [
    
    url(r'^users/login', User.as_view()),
]
