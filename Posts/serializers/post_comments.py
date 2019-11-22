from rest_framework import serializers
from Posts.models import PostComments


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['comment', 'parent']


class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['post', 'comment', 'parent']
