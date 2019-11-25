from rest_framework import serializers
from Auth.models import Followers


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = ['follower', ]
