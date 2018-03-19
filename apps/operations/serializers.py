#-*-coding:utf-8-*-
from rest_framework import serializers
from operations.models import Collection,Issue

class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields="__all__"

    def create(self, validated_data):
        return Collection.objects.create(**validated_data)


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields="__all__"

    def create(self, validated_data):
        return Issue.objects.create(**validated_data)