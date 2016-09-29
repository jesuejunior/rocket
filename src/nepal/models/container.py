# encoding: utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models
from nepal.models.node import Node


class Container(models.Model):
    """
        Container model
    """
    name = models.CharField(max_length=50, verbose_name='Naem of container')
    nodes = models.ManyToManyField(Node, db_table='container_has_node',
        related_name='containers', verbose_name='Container')
    config = JSONField()

    class Meta:
        db_table = u'container'
        verbose_name = 'Container'
