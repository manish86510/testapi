from rest_framework import serializers
from Auth.models import WorkPlace


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ["name", "position", "city", "description", "working_from", "working_till"]
