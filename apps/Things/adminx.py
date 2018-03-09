# _*_ coding:utf-8 _*_
from .models import Equipment, Software, Technology
import xadmin


class EquipmentAdmin(object):
    list_display = ['equip_id', 'equip_type', 'equip_name', 'equip_owner', 'equip_expense', 'equip_price']
    search_fields = ['equip_id', 'equip_type', 'equip_name', 'equip_owner', 'equip_expense', 'equip_price']
    list_filter = ['equip_id', 'equip_type', 'equip_name', 'equip_owner', 'equip_expense', 'equip_price']


class SoftwareAdmin(object):
    list_display = ['software_id', 'software_type', 'software_name', 'software_owner', 'software_expense', 'software_price']
    search_fields = ['software_id', 'software_type', 'software_name', 'software_owner', 'software_expense', 'software_price']
    list_filter = ['software_id', 'software_type', 'software_name', 'software_owner', 'software_expense', 'software_price']


class TechnologyAdmin(object):
    list_display = ['tech_id', 'tech_type', 'tech_name', 'tech_owner', 'tech_price']
    search_fields = ['tech_id', 'tech_type', 'tech_name', 'tech_owner', 'tech_price']
    list_filter = ['tech_id', 'tech_type', 'tech_name', 'tech_owner', 'tech_price']


xadmin.site.register(Equipment, EquipmentAdmin)
xadmin.site.register(Software, SoftwareAdmin)
xadmin.site.register(Technology, TechnologyAdmin)


