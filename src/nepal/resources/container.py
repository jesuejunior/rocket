# encoding: utf-8
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from nepal.models.container import Container
from nepal.serializers.container import ContainerSerializer


class ContainerView(APIView):
    """
    List all containers, or create a new container.
    """
    def get(self, request, format=None):
        action = self.request.query_params.get('action')
        if action == 'count':
            containers = Container.objects.count()
            return Response({'result': containers})
        containers = Container.objects.all()
        serializer = ContainerSerializer(containers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContainerDetail(APIView):
    """
    Retrieve, update or delete a container instance.
    """
    def get_object(self, pk):
        try:
            return Container.objects.get(pk=pk)
        except Container.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        container = self.get_object(pk)
        serializer = ContainerSerializer(container)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        container = self.get_object(pk)
        serializer = ContainerSerializer(container, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        container = self.get_object(pk)
        container.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
