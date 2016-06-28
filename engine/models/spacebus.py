# encoding: utf-8
from django.db import models

from engine.models.container import Container


class Spacebus(models.Model):
    """
    """
    name = models.CharField(max_length=40)
    container = models.ManyToManyField(Container,
                                       related_name='spacebus',
                                       db_table='spacebus_has_container',
                                       null=True,
                                       blank=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = u'spacebus'
        verbose_name = 'Spacebus'