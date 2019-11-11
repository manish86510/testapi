from rest_framework import serializers
from .models import *


# Created postserializer to convert the post model to json for creating posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = '__all__'


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = '__all__'


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = '__all__'
