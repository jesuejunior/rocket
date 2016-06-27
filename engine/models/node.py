# encoding: utf-8
from django.db import models


class Node(models.Model):

    """
    """
    name = models.CharField(max_length=150)
    so = models.CharField(max_length=40)
    provider = models.CharField(max_length=20)
    ip = models.IPAddressField()
    fqdn = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=22) # It'll change to encrypted field
    private_key = models.CharField(max_length=200) # It'll change to encrypted field
    ready = models.BooleanField(default=False)

    class Meta:
        db_table = u'node'
        verbose_name = 'Node'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'so': self.so,
            'provider': self.provider,
            'ip': str(self.ip),
            'fqdn': self.fqdn,
            'username': self.username,
            'password': self.password,
            'private_key': self.private_key
        }
