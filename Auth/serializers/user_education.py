from rest_framework import serializers
from Auth.models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for', 'user']
        # fields = "__all__"


class EducationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for']
        # fields = "__all__"
