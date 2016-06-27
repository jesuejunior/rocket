# encoding: utf-8
from django.contrib.postgres.fields import JSONField
from django.db import models


class Container(models.Model):

    """
        Container model
    """
    name = models.CharField(max_length=50)
    config = JSONField()

    class Meta:
        db_table = u'container'
        verbose_name = 'Container'