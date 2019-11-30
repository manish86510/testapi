from rest_framework import serializers
from Posts.serializers.post import PostSerializer
from Posts.serializers.post_media import PostMediaSerializer
from Posts.serializers.post_comments import PostCommentSerializer
from Posts.serializers.post_likes import PostLikeSerializer
from Posts.serializers.post_share import PostShareSerializer
from Posts.serializers.post_tag import PostTagSerializer
from Auth.serializers.user import UserSerializer
from Posts.models import Post
from django.contrib.postgres.fields import JSONField



class GetFullPostInfoSerializer(serializers.Serializer):
    post = PostSerializer(help_text="Help text for post")
    media = JSONField(blank=True, default=dict)
    comments = JSONField(blank=True, default=dict)
    likes = JSONField(blank=True, default=dict)
    shares = JSONField(blank=True, default=dict)
    tags = JSONField(blank=True, default=dict)
    # user = UserSerializer(help_text="Help text for post User")
    # import pdb
    # pdb.set_trace()

    class Meta:
        fields = '__all__'

