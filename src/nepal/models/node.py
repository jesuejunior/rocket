# encoding: utf-8
from django.db import models

PROVIDERS = ('aws', 'rackspace', 'vmware', 'digital ocean', 'linode')


class Node(models.Model):
    """
    """
    name = models.CharField(max_length=150)
    so = models.CharField(max_length=40)
    provider = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    docker_port = models.IntegerField(default=2375)
    fqdn = models.CharField(max_length=50, null=True, blank=True)
    ready = models.BooleanField(default=False)

    class Meta:
        db_table = u'node'
        verbose_name = 'Node'
