from rest_framework import serializers
from Auth.models import MyProjects


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ['id', 'project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name', 'user']
        # fields = "__all__"


class ProjectsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ['id', 'project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name']
        # fields = "__all__"
