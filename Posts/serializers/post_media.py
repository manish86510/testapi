from rest_framework import serializers
from Posts.models import PostMedia


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['file', 'file_type']


class PostMediaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id', 'post', 'file', 'file_type']
