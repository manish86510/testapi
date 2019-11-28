from rest_framework import serializers
from Posts.models import PostLikes


class PostLikeSerializer(serializers.ModelSerializer):
    activity = serializers.CharField(max_length=200, read_only=False)

    class Meta:
        model = PostLikes
        fields = ['activity']


class PostLikeCreateSerializer(serializers.ModelSerializer):
    activity = serializers.CharField(max_length=200, read_only=False)

    class Meta:
        model = PostLikes
        fields = ['post', 'activity']
