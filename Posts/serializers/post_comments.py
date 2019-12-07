from rest_framework import serializers
from Posts.models import PostComments
from Auth.serializers import *


class PostCommentSerializer(serializers.ModelSerializer):
    user = user.UserCustomFieldSerializer()

    class Meta:
        model = PostComments
        fields = ['post', 'comment', 'parent', 'user']


class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['post', 'comment', 'parent']
