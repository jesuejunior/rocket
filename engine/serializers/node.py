# encoding: utf-8
from rest_framework import serializers
from engine.models.node import Node


class NodeSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Node
        fields = ('id', 'name', 'so', 'provider', 'ip',
                  'docker_port', 'fqdn', 'username', 'password',
                  'private_key', 'ready')
