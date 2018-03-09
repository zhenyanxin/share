# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserMust(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u"用户ID")
    nick_name = models.CharField(max_length=20,  default="", null=False, blank=False, verbose_name=u"昵称")
    password = models.CharField(max_length=20, default="", null=False, blank=False, verbose_name=u"密码")
    phone = models.CharField(max_length=11, null=False, blank=False, verbose_name=u"手机号")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.nick_name


class UserComplete(models.Model):
    user_id = models.ForeignKey(UserMust, verbose_name=u"用户ID")
    user_name = models.CharField(max_length=10, default=u"", verbose_name=u"用户姓名")
    identity = models.CharField(max_length=20, default=u"", verbose_name=u"身份证号")
    bank = models.CharField(max_length=20, default=u"", verbose_name=u"开户行")
    bank_number = models.CharField(max_length=30, default=u"", verbose_name=u"银行卡号")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    image = models.ImageField(upload_to="users/%Y/%m", default=u"users/default.png", max_length=100, verbose_name="用户头像图片")

    class Meta:
        verbose_name = "用户完善信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user_name


class UserSelectable(models.Model):
    user_id = models.ForeignKey(UserMust, verbose_name=u"用户ID")
    nick_name = models.CharField(max_length=20,  default="", null=False, blank=False, verbose_name=u"昵称")
    education = models.CharField(max_length=20, default="", verbose_name="学历")
    qq = models.CharField(max_length=20, default="", verbose_name="QQ号")
    wechat = models.CharField(max_length=30, default="", verbose_name="微信号")

    class Meta:
        verbose_name = "用户可选信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.nick_name



