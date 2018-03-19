from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import CollectionsSerializer,IssuesSerializer
from .models import Collection,Issue

class CollectionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class CollectionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = CollectionPagination


class IssuePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class IssuesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    pagination_class = IssuePagination