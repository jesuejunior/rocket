# encoding: utf-8
from django.conf.urls import *

from engine.resources.node import NodeDetail, NodeView

urlpatterns = [
	url(r'(?P<pk>[0-9]+)', NodeDetail.as_view()),
	url(r'$', NodeView.as_view()),
]
