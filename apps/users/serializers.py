#-*-coding:utf-8-*-

from rest_framework import serializers
from .models import UserMust,UserComplete,UserSelectable,VerifyCode


class UserMustsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMust
        fields="__all__"

    def create(self, validated_data):
        return UserMust.objects.create(**validated_data)


class UserCompletesSerializer(serializers.ModelSerializer):
    user_id=UserMustsSerializer
    class Meta:
        model = UserComplete
        fields="__all__"

    def create(self, validated_data):
        return UserComplete.objects.create(**validated_data)


class UserSelectablesSerializer(serializers.ModelSerializer):
    user_id=UserMustsSerializer
    class Meta:
        model = UserSelectable
        fields="__all__"

    def create(self, validated_data):
        return UserSelectable.objects.create(**validated_data)


class VerifyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields="__all__"

    def create(self, validated_data):
        return VerifyCode.objects.create(**validated_data)