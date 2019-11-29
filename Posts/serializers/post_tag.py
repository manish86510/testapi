from rest_framework import serializers
from Posts.models import PostTag


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'
