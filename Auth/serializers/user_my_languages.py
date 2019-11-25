from rest_framework import serializers
from Auth.models import MyLanguage


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ["name", "read", "write", "speak"]
