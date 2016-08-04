# encoding: utf-8
from django.conf.urls import *

from engine.resources.container import ContainerDetail, ContainerView
from engine.resources.node import NodeDetail, NodeView

urlpatterns = [
	url(r'^nodes/(?P<pk>[0-9]+)', NodeDetail.as_view()),
	url(r'^nodes', NodeView.as_view()),
	url(r'^containers/(?P<pk>[0-9]+)', ContainerDetail.as_view()),
	url(r'^containers', ContainerView.as_view()),
]
