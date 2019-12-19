from rest_framework import serializers
from Posts.models import PostComments
from Auth.serializers.user import UserCustomFieldSerializer


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserCustomFieldSerializer()
    children = serializers.SerializerMethodField()

    class Meta:
        model = PostComments
        fields = ['id', 'post', 'comment', 'parent', 'user', 'children']

    def get_children(self, obj):
        if obj.parent:
            post_obj = PostComments.objects.filter(parent=obj.id)
            abc = PostCommentSerializer(post_obj, many=True).data
            abcc=0
            return abc


class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['post', 'comment', 'parent']
