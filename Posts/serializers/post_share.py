from rest_framework import serializers
from Posts.models import PostShare


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = ['description']


class PostShareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = ['post', 'description']
