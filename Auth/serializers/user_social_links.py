from rest_framework import serializers
from Auth.models import SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "name", "unique_id", 'user']
        # fields = "__all__"


class SocialLinksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["id", "name", "unique_id"]
        # fields = "__all__"
