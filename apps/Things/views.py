from django.shortcuts import render

# Create your views here.
from .serializers import Equip_typesSerializer,EquipmentsSerializer,SoftwaresSerializer,TechnologiesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equip_type,Equipment,Software,Technology
from rest_framework import status

class Equip_typesListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        equip_types = Equip_type.objects.all()[:10]
        equip_types_serializer = EquipmentsSerializer(equip_types, many=True)
        return Response(equip_types_serializer.data)

    def post(self, request, format=None):
        serializer = Equip_typesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SoftwaresListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        softwares = Software.objects.all()[:10]
        softwares_serializer = EquipmentsSerializer(softwares, many=True)
        return Response(softwares_serializer.data)

    def post(self, request, format=None):
        serializer = SoftwaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechnologiesListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        technologies = Technology.objects.all()[:10]
        technologies_serializer = TechnologiesSerializer(equipments, many=True)
        return Response(technologies_serializer.data)

    def post(self, request, format=None):
        serializer = TechnologiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        equipments = Equipment.objects.all()[:10]
        equipments_serializer = EquipmentsSerializer(equipments, many=True)
        return Response(equipments_serializer.data)

    def post(self, request, format=None):
        serializer = EquipmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
