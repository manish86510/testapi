from rest_framework import serializers
from Posts.models import PostTag
from Auth.serializers.user import *


class PostTagSerializer(serializers.ModelSerializer):
    tag_user = UserCustomFieldSerializer()

    class Meta:
        model = PostTag
        fields = ('id', 'post', 'tag_user', 'tagged_users')


class PostTagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ('post', 'tag_user', 'tagged_users')