# encoding: utf-8
import simplejson as json
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from nepal.models.node import Node
from nepal.serializers.node import NodeSerializer


class NodeView(APIView):
    """
    List all nodes, or create a new node.
    """
    def get(self, request, format=None):
        action = self.request.query_params.get('action', None)
        if action == 'count':
            nodes = Node.objects.count()
            return Response({'result': nodes})
        nodes = Node.objects.all()
        serializer = NodeSerializer(nodes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NodeDetail(APIView):
    """
    Retrieve, update or delete a node instance.
    """
    def get_object(self, pk):
        try:
            return Node.objects.get(pk=pk)
        except Node.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        node = self.get_object(pk)
        serializer = NodeSerializer(node)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        node = self.get_object(pk)
        serializer = NodeSerializer(node, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        node = self.get_object(pk)
        node.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
