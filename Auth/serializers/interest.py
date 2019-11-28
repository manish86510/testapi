from rest_framework import serializers
from Auth.models import Interests


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interests
        fields = '__all__'
