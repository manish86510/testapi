from rest_framework import serializers
from Auth.models import MyInterest


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = ["interest_code",]
