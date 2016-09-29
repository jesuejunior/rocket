# encoding: utf-8
# flake8: noqa
from django.conf.urls import *

from nepal.resources.container import ContainerDetail, ContainerView
from nepal.resources.node import NodeDetail, NodeView

urlpatterns = [
    url(r'^nodes/(?P<pk>[0-9]+)', NodeDetail.as_view()),
    url(r'^nodes', NodeView.as_view()),
    url(r'^containers/(?P<pk>[0-9]+)', ContainerDetail.as_view()),
    url(r'^containers', ContainerView.as_view()),
]
