from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from datetime import datetime
UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        queryset = ''

        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get(self):
        user = UserModel.objects.get()
        return user


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for', 'user')

    def create(self, validated_data):
        email = validated_data['email']
        education = Education(
            school_college_name = validated_data['school_college_name'],
            description = validated_data['session_from'],
            session_from = datetime.strptime(validated_data['session_from'], "%Y-%m-%d").date(),
            session_to = datetime.strptime(validated_data['session_to'], "%Y-%m-%d").date(),
            attended_for = validated_data['attended_for'],
            user = UserModel.objects.get(email=email)
        )
        education.save()
        return education


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = ('id', 'place_name', 'lat_long', 'from_date', 'to_date', 'user')
        read_only_fields = ('id',)

    def create(self, validated_data):
        email = validated_data['email']
        places = MyPlaces.objects.create(
            place_name = validated_data['place_name'],
            lat_long = validated_data['lat_long'],
            from_date = datetime.strptime(validated_data['from_date'], "%Y-%m-%d").date(),
            to_date = datetime.strptime(validated_data['to_date'], "%Y-%m-%d").date(),
            user = UserModel.objects.get(email=email)
        )
        return places


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ('id', 'name', 'position', 'city', 'description', 'working_from', 'working_till', 'user')
        read_only_fields = ('id',)

    def create(self, validated_data):
        email = validated_data['email']
        work = WorkPlace.objects.create(
            name=validated_data['name'],
            position=validated_data['position'],
            city=validated_data['city'],
            description=validated_data['description'],
            working_from=datetime.strptime(validated_data['working_from'], "%Y-%m-%d").date(),
            working_till=datetime.strptime(validated_data['working_till'], "%Y-%m-%d").date(),
            user=UserModel.objects.get(email=email)
        )
        return work


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ('id', 'project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name', 'user')
        read_only_fields = ('id',)

    def create(self, validated_data):
        email = validated_data['email']
        project = MyProjects.objects.create(
            project_title=validated_data['project_title'],
            description=validated_data['description'],
            skills=validated_data['skills'],
            start_date=validated_data['start_date'],
            end_date=datetime.strptime(validated_data['end_date'], "%Y-%m-%d").date(),
            team_size=validated_data['team_size'],
            client_name=validated_data['client_name'],
            user=UserModel.objects.get(email=email)
        )
        return project


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ('id', 'user', 'name', 'read', 'write', 'speak')
        read_only_fields = ('id',)

    def create(self, validated_data):
        email = validated_data['email']
        language = MyLanguage.objects.create(
            user=UserModel.objects.get(email=email),
            name=validated_data['project_title'],
            read=validated_data['description'],
            write=validated_data['skills'],
            speak=validated_data['start_date']
        )
        return language
