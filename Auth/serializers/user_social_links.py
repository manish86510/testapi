from rest_framework import serializers
from Auth.models import SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["name", "unique_id"]
