from rest_framework import serializers
from ..models import Followers
from ..serializers.user import UserSerializer


class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()

    class Meta:
        model = Followers
        fields = ['id', 'follower', 'user']
        # fields = "__all__"


class FollowerCreateSerializer(serializers.ModelSerializer):
    following = serializers.IntegerField(required=True)

    class Meta:
        model = Followers
        fields = ['id', 'following']
