from rest_framework import serializers
from Auth.models import MyProjects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ['project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name']
