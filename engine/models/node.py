# encoding: utf-8
from django.db import models

PROVIDERS = ('aws', 'rackspace', 'vmware', 'digital ocean', 'linode', )

class Node(models.Model):

    """
    """
    name = models.CharField(max_length=150)
    so = models.CharField(max_length=40)
    provider = models.CharField(choices=PROVIDERS, max_length=20, default='digital ocean')
    ip = models.IPAddressField()
    fqdn = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=22) # It'll change to encrypted field
    private_key = models.CharField(max_length=200) # It'll change to encrypted field
    ready = models.BooleanField(default=False)

    class Meta:
        db_table = u'node'
        verbose_name = 'Node'
