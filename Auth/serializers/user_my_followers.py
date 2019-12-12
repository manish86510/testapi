from rest_framework import serializers
from Auth.models import *
from Auth.serializers.user import *


class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()

    class Meta:
        model = Followers
        fields = ['id', 'follower', 'user']
        # fields = "__all__"


class FollowerCreateSerializer(serializers.ModelSerializer):
    follower = serializers.IntegerField(required=True)

    class Meta:
        model = Followers
        fields = ['id', 'follower']
