# _*_coding:utf-8_*_


from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#外键，主键，无Double类型

class Equipment(models.Model):
    equip_id = models.AutoField(primary_key=True, verbose_name=u"设备ID")
    equip_type = models.CharField(choices=(("Equipment", u"设备"), ("Software", u"软件"), ("Technology", u"技术")), max_length=10, verbose_name=u"最初分类")
    equip_name = models.CharField(max_length=100, verbose_name=u"设备名称")
    produce_date = models.DateTimeField(default=datetime.now, verbose_name=u"生产日期")
    equip_over = models.DateTimeField(default=datetime.now, verbose_name=u"到期年限")
    equip_owner = models.IntegerField(default=0, verbose_name=u"设备所属")
    equip_expense = models.FloatField(default=0.0, verbose_name=u"设备价格")
    equip_start = models.DateTimeField(default=datetime.now, verbose_name=u"出租开始时间")
    equip_end = models.DateTimeField(default=datetime.now, verbose_name=u"出租结束时间")
    equip_price = models.FloatField(default=0.0, verbose_name=u"出租费用")
    equip_picture = models.CharField(max_length=100, verbose_name=u"设备图片")
    equip_typeb = models.CharField(max_length=100, verbose_name=u"设备大类别")
    equip_types = models.CharField(max_length=100, verbose_name=u"设备小类别")
    equip_parameter = models.TextField(verbose_name=u"性能参数")
    equip_place = models.TextField(verbose_name=u"地点")
    equip_comment = models.CharField(max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"设备"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return self.equip_name


class Software(models.Model):
    software_id = models.AutoField(primary_key=True, verbose_name=u"设备ID")
    software_type = models.CharField(choices=(("Equipment", u"设备"), ("Software", u"软件"), ("Technology", u"技术")), max_length= 10, verbose_name=u"最初分类")
    software_name = models.CharField(max_length=100, verbose_name=u"软件名称")
    software_owner = models.IntegerField(default=0, verbose_name=u"软件所属")
    software_expense = models.FloatField(default=0.0, verbose_name=u"软件价格")
    software_start = models.DateTimeField(default=datetime.now, verbose_name=u"出租开始时间")
    software_end = models.DateTimeField(default=datetime.now, verbose_name=u"出租结束时间")
    software_price = models.FloatField(default=0.0, verbose_name=u"出租费用")
    software_image = models.CharField(max_length=100, verbose_name=u"软件图片")
    oftware_typeb =  models.CharField(max_length=100, verbose_name=u"软件大类别")
    equip_types = models.CharField(max_length=100, verbose_name=u"软件小类别")
    software_describe = models.TextField(verbose_name=u"软件描述")
    os = models.CharField(max_length=100, verbose_name=u"运行平台")
    software_comment = models.CharField(max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"软件"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return self.software_name


class Technology(models.Model):
    tech_id = models.AutoField(primary_key=True, verbose_name=u"技术ID")
    tech_type = models.CharField(choices=(("Equipment", u"设备"), ("Software", u"软件"), ("Technology", u"技术")), max_length= 10, verbose_name=u"最初分类")
    tech_name = models.CharField(max_length=100, verbose_name=u"技术名称")
    tech_info = models.CharField(max_length=300, verbose_name=u"技术服务信息")
    tech_typeb = models.CharField(max_length=100, verbose_name=u"技术大类别")
    tech_types = models.CharField(max_length=100, verbose_name=u"技术小类别")
    tech_owner = models.IntegerField(default=0, verbose_name=u"技术所属")
    tech_price = models.FloatField(default=0.0, verbose_name=u"技术价格")
    tech_image = models.CharField(max_length=100, verbose_name=u"技术图片")
    tech_commet = models.CharField(max_length=300, verbose_name=u"备注")

    class Meta:
        verbose_name = u"技术"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return self.tech_name


class Equip_type(models.Model):
    type_id1 = models.AutoField(primary_key=True, verbose_name=u"设备分类ID")
    type_big1 = models.CharField(max_length=100, verbose_name=u"设备大类别")
    type_small1 = models.CharField(max_length=100, verbose_name=u"设备小类别")

    class Meta:
        verbose_name = u"设备分类"
        verbose_name_plural = verbose_name

    def _unicode_(self):
        return  self.type_id1











