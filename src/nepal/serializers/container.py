# encoding: utf-8
from rest_framework import serializers

from nepal.models import Container
from nepal.serializers.node import NodeSerializer


class ContainerSerializer(serializers.ModelSerializer):
    """
    """
    nodes = NodeSerializer(many=True)

    class Meta:
        model = Container
        fields = ('id', 'name','hosts', 'config')

    def create(self, validated_data):
        nodes_data = validated_data.pop('nodes')
        container = Container.objects.create(**validated_data)
        for node in nodes_data:
            Node.objects.create(container=container, **node)
        return container

