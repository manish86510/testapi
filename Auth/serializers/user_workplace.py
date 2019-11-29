from rest_framework import serializers
from Auth.models import WorkPlace


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ["id", "name", "position", "city", "description", "working_from", "working_till", 'user']
        # fields = "__all__"


class WorkplaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ["id", "name", "position", "city", "description", "working_from", "working_till"]
        # fields = "__all__"
