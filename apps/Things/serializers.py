#-*-coding:utf-8-*-
from rest_framework import serializers
from Things.models import Equipment,Software,Technology,Equip_type


class Equip_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equip_type
        fields="__all__"


class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields="__all__"

    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)


class SoftwaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields="__all__"

    def create(self, validated_data):
        return Software.objects.create(**validated_data)



class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields="__all__"
        
    def create(self, validated_data):
        return Technology.objects.create(**validated_data)