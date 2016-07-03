# encoding: utf-8
from django.conf.urls import *

from engine.resources.node import NodeDetail, NodeList

urlpatterns = [
	url(r'$', NodeList.as_view()),
	url(r'(?P<pk>[0-9]+)$', NodeDetail.as_view()),
]
