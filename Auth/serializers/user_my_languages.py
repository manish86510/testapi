from rest_framework import serializers
from Auth.models import MyLanguage


class MyLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ["id", "name", "read", "write", "speak", 'user']
        # fields = "__all__"


class MyLanguageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ["id", "name", "read", "write", "speak"]
        # fields = "__all__"
