from rest_framework import serializers
# from .user_field import CurrentUserID
from Posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['about_post', 'tags', 'is_public', 'post_type', 'target_audience', 'user']
        read_only_fields = ['user', ]
