from rest_framework import serializers
from Auth.models import Languages


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = '__all__'
