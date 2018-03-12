# -*- coding: utf-8 -*-

import xadmin
from .models import UserMust, UserComplete, UserSelectable,VerifyCode
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "地质设备共享"
    site_footer = "公司"
    menu_style = "accordion"


class UserMustAdmin(object):
    list_display = ['id', 'nick_name', 'phone']
    search_fields = ['id', 'nick_name', 'phone']
    list_filter = ['id', 'nick_name', 'phone']


class UserCompleteAdmin(object):
    list_display = ['user_id', 'user_name', 'identity', 'gender', 'address']
    search_fields = ['user_id', 'user_name', 'identity', 'gender', 'address']
    list_filter = ['user_id', 'user_name', 'identity', 'gender', 'address']


class UserSelectableAdmin(object):
    list_display = ['user_id', 'education', 'qq', 'wechat']
    search_fields = ['user_id', 'education', 'qq', 'wechat']
    list_filter = ['user_id', 'education', 'qq', 'wechat']


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile',  'add_time']
    search_fields = ['code', 'mobile']
    list_filter = ['code', 'mobile',  'add_time']


xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(UserMust, UserMustAdmin)
xadmin.site.register(UserComplete, UserCompleteAdmin)
xadmin.site.register(UserSelectable, UserSelectableAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
