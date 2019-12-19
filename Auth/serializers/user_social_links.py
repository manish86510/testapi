from rest_framework import serializers
from Auth.models import SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "name", "url", 'user']
        # fields = "__all__"


class SocialLinksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "name", "url"]
        # fields = "__all__"
