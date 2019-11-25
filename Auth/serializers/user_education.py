from rest_framework import serializers
from Auth.models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['school_college_name', 'description', 'session_from', 'session_to', 'attended_for']
