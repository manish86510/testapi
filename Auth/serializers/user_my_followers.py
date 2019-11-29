from rest_framework import serializers
from Auth.models import Followers


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ['id', 'follower', 'user']
        # fields = "__all__"


class FollowerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ['id', 'follower']
        # fields = "__all__"
