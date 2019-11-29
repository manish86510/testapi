from rest_framework import serializers
from Auth.models import MyInterest


class MyInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = ["id", "interest_code", 'user']
        # fields = "__all__"


class MyInterestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = ["id", "interest_code"]
        # fields = "__all__"
