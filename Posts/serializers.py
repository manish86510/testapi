from rest_framework import serializers
from django.contrib.auth import get_user_model
from Posts.models import Post
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
        fields = ('id', 'about_post', 'tags', 'created_by', 'user', 'is_public', 'target_audience_interests', 'post_type')
        write_only_fields = ()
        read_only_fields = ('id', )

    def create(self, validated_data):
        queryset = ''
        post = Post.objects.create(
            about_post = validated_data['about_post'],
            tags = validated_data['tags'],
            created_by = validated_data['created_by'],
            user = User.objects.get(pk=1),
            is_public = validated_data['is_public'],
            target_audience_interests = validated_data['target_audience_interests'],
            post_type = validated_data['post_type']
        )
        post.save()
        return post

    def get(self):
        post = Post.objects.get()
