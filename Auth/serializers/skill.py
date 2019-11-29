from rest_framework import serializers
from Auth.models import Skills


class SkillCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = "__all__"
