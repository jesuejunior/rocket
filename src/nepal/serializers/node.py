# encoding: utf-8
from rest_framework import serializers
from nepal.models.node import Node


class NodeSerializer(serializers.ModelSerializer):
    """
        Node serializer
    """
    class Meta:
        model = Node
        fields = ('id', 'name', 'so', 'provider', 'ip',
                  'docker_port', 'fqdn', 'ready')
