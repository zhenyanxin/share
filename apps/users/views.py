from django.shortcuts import render

# Create your views here.

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import UserMustsSerializer,UserCompletesSerializer,UserSelectablesSerializer,VerifyCodesSerializer
from .models import UserSelectable,UserMust,UserComplete,VerifyCode


class UserSelectablePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UserSelectablesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = UserSelectable.objects.all()
    serializer_class = UserSelectablesSerializer
    pagination_class = UserSelectablePagination


class UserCompletePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UserCompletesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = UserComplete.objects.all()
    serializer_class = UserCompletesSerializer
    pagination_class = UserCompletePagination


class UserMustPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UserMustsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = UserMust.objects.all()
    serializer_class = UserMustsSerializer
    pagination_class = UserMustPagination


class VerifyCodePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class VerifyCodesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodesSerializer
    pagination_class = VerifyCodePagination
