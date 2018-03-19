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
from ss.settings import MEDIA_ROOT
#from django.contrib import admin
import xadmin
#from Things.views_base import EquipmentsListView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from Things.views import EquipmentsViewSet,SoftwaresViewSet,TechnologiesViewSet
from users.views import UserCompletesViewSet,UserMustsViewSet,UserSelectablesViewSet,VerifyCodesViewSet
from operations.views import IssuesViewSet,CollectionsViewSet
from django.views.static import serve

router = DefaultRouter()

router.register(r'equipments', EquipmentsViewSet)
router.register(r'softwares', SoftwaresViewSet)
router.register(r'technologies', TechnologiesViewSet)
router.register(r'issue', IssuesViewSet)
router.register(r'collection', CollectionsViewSet)
router.register(r'user_must',UserMustsViewSet)
router.register(r'user_completes',UserCompletesViewSet)
router.register(r'user_selectable',UserSelectablesViewSet)
router.register(r'verifyCodes',VerifyCodesViewSet)


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^',include(router.urls)),

    url(r'docs/',include_docs_urls(title='地质设备共享')),

    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework'))

]
