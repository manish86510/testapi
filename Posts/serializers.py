from rest_framework import serializers
from .models import *


# Created postserializer to convert the post model to json for creating posts
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'about_post', 'tags', 'created_by', 'is_public', 'target_audience_interests', 'post_type'
        )


class PostUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = Post
        fields = (
            'id', 'about_post', 'tags', 'created_by', 'is_public', 'target_audience_interests', 'post_type'
        )


class PostGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = Post
        fields = ('id',)


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = '__all__'


class PostMediaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ('post', 'file', 'file_type')


class PostMediaUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostMedia
        fields = ('id', 'post', 'file', 'file_type')


class PostMediaGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostMedia
        fields = ('id',)


class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = '__all__'


class PostLikesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = ('post', 'activity')


# class PostLikesUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostLikes
#         fields = ('id', 'post', 'activity')


class PostLikesGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostLikes
        fields = ('id',)


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'


class PostCommentsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ('post', 'parent', 'comment')


class PostCommentsUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostComments
        fields = ('id', 'comment')


class PostCommentsGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostComments
        fields = ('id',)


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = '__all__'


class PostShareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostShare
        fields = ('post', 'description')


class PostShareUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostShare
        fields = ('id', 'post', 'description')


class PostShareGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = PostShare
        fields = ('id',)
