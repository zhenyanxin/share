#-*-coding:utf-8-*-
from datetime import datetime
from rest_framework import serializers
from Things.models import Equipment,Software,Technology,Equip_type


class Equip_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equip_type;
        fields="__all__"


class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment;
        fields="__all__"


class SoftwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software;
        fields="__all__"


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology;
        fields="__all__"