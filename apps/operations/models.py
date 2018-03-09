# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from users.models import UserMust


class Collection(models.Model):
    user_id = models.ForeignKey(UserMust, verbose_name=u"用户ID")
    collect_type = models.CharField(max_length=3,
                                    choices=(("equipment", "设备"), ("software", "软件"), ("technology", "技术")),
                                    default="equipment",
                                    verbose_name="产品最初分类")
    product_id = models.IntegerField(default=0, verbose_name=u"收藏产品ID")
    product_image = models.ImageField(upload_to="product/%Y/%m", default=u"product/default.png", max_length=100, verbose_name="收藏产品图片")
    product_name = models.CharField(max_length=30, verbose_name="收藏产品名称")
    product_price = models.FloatField(default=0, verbose_name="费用")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product_name


class Issue(models.Model):
    user_id = models.ForeignKey(UserMust, verbose_name=u"用户ID")
    issue_type = models.CharField(max_length=3,
                                  choices=(("equipment", "设备"), ("software", "软件"), ("technology", "技术")),
                                  default="equipment",
                                  verbose_name="产品最初分类")
    product_id = models.IntegerField(default=0, verbose_name=u"发布产品ID")
    issue_image = models.ImageField(upload_to="product/%Y/%m", default=u"product/default.png", max_length=100, verbose_name="发布产品图片")
    product_name = models.CharField(max_length=30, verbose_name="发布产品名称")
    issue_price = models.FloatField(default=0, verbose_name="费用")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "用户发布"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product_name





