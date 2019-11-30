from rest_framework import serializers
from Posts.serializers.post import PostSerializer
from Posts.serializers.post_media import PostMediaSerializer
from Posts.serializers.post_comments import PostCommentSerializer
from Posts.serializers.post_likes import PostLikeSerializer
from Posts.serializers.post_share import PostShareSerializer
from Posts.serializers.post_tag import PostTagSerializer
from Auth.serializers.user import UserSerializer
from Posts.models import Post


class GetFullPostInfoSerializer(serializers.Serializer):
    post = PostSerializer(help_text="Help text for post")
    media = PostMediaSerializer(help_text="Help text for post media")
    comments = PostCommentSerializer(help_text="Help text for post comments")
    likes = PostLikeSerializer(help_text="Help text for post likes")
    shares = PostShareSerializer(help_text="Help text for post shares")
    tags = PostTagSerializer(help_text="Help text for post tags")
    # user = UserSerializer(help_text="Help text for post User")
    # import pdb
    # pdb.set_trace()

    class Meta:
        fields = '__all__'

