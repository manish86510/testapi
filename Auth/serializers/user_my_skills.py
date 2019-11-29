from rest_framework import serializers
from Auth.models import MySkills


class MySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = ["id", "skill", 'user']
        # fields = "__all__"

class MySkillCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = ["id", "skill"]
        # fields = "__all__"