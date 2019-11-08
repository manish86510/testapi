from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from Auth.models import *

# taken for reference
UserModel = get_user_model()


# # Created postserializer to convert the post model to json for view
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post


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
