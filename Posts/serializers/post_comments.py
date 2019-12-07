from rest_framework import serializers
from Posts.models import PostComments
from Auth.serializers import *


class PostCommentSerializer(serializers.ModelSerializer):
    user = user.UserCustomFieldSerializer()
    parent = serializers.SerializerMethodField()

    class Meta:
        model = PostComments
        fields = ['id', 'post', 'comment', 'parent', 'user']

    def get_parent(self, obj):
        # import pdb
        # pdb.set_trace()
        if obj.parent:
            post_obj = PostComments.objects.filter(parent=obj.id)
            return PostCommentSerializer(post_obj, many=True).data



class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['post', 'comment', 'parent']
