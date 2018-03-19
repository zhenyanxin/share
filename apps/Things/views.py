#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import Equip_typesSerializer,EquipmentsSerializer,SoftwaresSerializer,TechnologiesSerializer
from .models import Equip_type,Equipment,Software,Technology

class Equip_typesListView(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Equip_type.objects.all()
    serializer_class = Equip_typesSerializer


class SoftwarePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SoftwaresViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Software.objects.all()
    serializer_class = SoftwaresSerializer
    pagination_class = SoftwarePagination


class TechnologyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class TechnologiesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    技术列表
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologiesSerializer
    pagination_class = TechnologyPagination


class EquipmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class EquipmentsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    设备列表
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentsSerializer
    pagination_class = EquipmentPagination

