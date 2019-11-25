from rest_framework import serializers
from Auth.models import MySkills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = ["skill",]
