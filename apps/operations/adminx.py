# -*- coding: utf-8 -*-

import xadmin
from .models import Collection, Issue


class CollectionAdmin(object):
    list_display = ['user_id', 'collect_type', 'product_name', 'product_price']
    search_fields = ['user_id', 'collect_type', 'product_name', 'product_price']
    list_filter = ['user_id', 'collect_type', 'product_name', 'product_price']


class IssueAdmin(object):
    list_display = ['user_id', 'issue_type', 'product_name', 'issue_price']
    search_fields = ['user_id', 'issue_type', 'product_name', 'issue_price']
    list_filter = ['user_id', 'issue_type', 'product_name', 'issue_price']


xadmin.site.register(Collection, CollectionAdmin)
xadmin.site.register(Issue, IssueAdmin)
