from rest_framework import serializers
# from .user_field import CurrentUserID
from Posts.models import Post
from .post_tag import *
from .post_likes import *
from .post_comments import *
from .post_media import *
from .post_share import *
from Auth.serializers.user import UserFollowerDetailSerializer


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
    tag = PostTagSerializer(many=True, source="post_tag")
    # post_comment = PostCommentSerializer(many=True)
    # post_like = PostLikeSerializer(many=True)
    # post_share = PostShareSerializer(many=True)
    post_media = PostMediaSerializer(many=True)
    user = UserFollowerDetailSerializer()
    is_like = serializers.SerializerMethodField(default=False)

    class Meta:
        model = Post
        fields = ('id', 'tag', 'post_media', 'about_post', 'tags',
                  'like_count', 'share_count', 'comment_count', 'points_earner', 'user', 'is_public', 'target_audience',
                  'post_type', 'is_like', 'created_on')

    def get_is_like(self, obj):
        # self.post_like
        like = PostLikes.objects.filter(post=obj, user=self.context.get('request').user).first()
        if like:
            return True
        return False
