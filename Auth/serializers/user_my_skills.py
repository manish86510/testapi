from rest_framework import serializers
from Auth.models import MySkills


class MySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = ["skill",]
