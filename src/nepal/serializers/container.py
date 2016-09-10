# encoding: utf-8
from rest_framework import serializers

from nepal.models.container import Container
from nepal.models.node import Node


class ContainerSerializer(serializers.ModelSerializer):
    """
    """
    nodes = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects)

    class Meta:
        model = Container
        fields = ('id', 'name', 'nodes', 'config')

    def create(self, validated_data):
        nodes_data = validated_data.pop('nodes')
        container = Container.objects.create(**validated_data)
        container.nodes.set(nodes_data, bulk=True)
        return container

    def update(self, instance, validated_data):
        nodes_data = validated_data.pop('nodes')
        instance.name = validated_data.get('name', instance.name)
        # TODO: Maybe it's a problem 
        instance.config = validated_data.get('config', instance.config)
        instance.nodes.set(nodes_data, bulk=True)
        instance.save()
        return instance

