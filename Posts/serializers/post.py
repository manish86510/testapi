from rest_framework import serializers
# from .user_field import CurrentUserID
from Posts.models import Post
from .post_tag import *
from .post_likes import *
from .post_comments import *
from .post_media import *
from .post_share import *
from Auth.serializers import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['about_post', 'tags', 'is_public', 'post_type', 'target_audience', 'user']
        read_only_fields = ['user', ]


class PostAllDetailSerializer(serializers.ModelSerializer):
    post_tag = PostTagSerializer(many=True)
    post_comment = PostCommentSerializer(many=True)
    post_like = PostLikeSerializer(many=True)
    post_share = PostShareSerializer(many=True)
    post_media = PostMediaSerializer(many=True)
    user = user.UserCustomFieldSerializer()

    class Meta:
        model = Post
        fields = ('post_tag', 'post_comment', 'post_like', 'post_share', 'post_media', 'about_post', 'tags',
                  'like_count', 'share_count', 'comment_count', 'points_earner', 'user', 'is_public', 'target_audience',
                  'post_type')
