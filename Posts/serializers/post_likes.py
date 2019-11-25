from rest_framework import serializers
from Posts.models import PostLikes


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = ['activity']


class PostLikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = ['post', 'activity']
