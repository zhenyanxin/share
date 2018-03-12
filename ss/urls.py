# _*_ encoding:utf-8 _*_

"""ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

#from django.contrib import admin
import xadmin
#from Things.views_base import EquipmentsListView
from rest_framework.documentation import include_docs_urls
from Things.views import EquipmentsListView
from django.views.static import serve

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'Things/$',EquipmentsListView.as_view(),name='equipment-list'),

    url(r'docs/',include_docs_urls(title='地质设备共享')),

    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))

]
