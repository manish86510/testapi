from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from .models import MyProjects

# from datetime import datetime

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


'''class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        '''


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'salutation', 'first_name', 'last_name', 'about', 'avatar',
            'cover_picture', 'skills', 'address', 'enlarge_url', 'date_of_birth',
            'birth_place', 'gender'
        )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class EducationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('school_college_name', 'description', 'session_from', 'session_to', 'attended_for')


class EducationUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = Education
        fields = ('id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for')
        write_only_fields = ('id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for')


class EducationGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = Education
        fields = ('id',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = '__all__'


class PlacePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = ('place_name', 'lat_long', 'from_date', 'to_date')


class PlaceUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyPlaces
        fields = ('id', 'place_name', 'lat_long', 'from_date', 'to_date')


class PlaceGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyPlaces
        fields = ('id',)


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = '__all__'


class WorkplacePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ('name', 'position', 'city', 'description', 'working_from', 'working_till')


class WorkplaceUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = WorkPlace
        fields = ('id', 'name', 'position', 'city', 'description', 'working_from', 'working_till')


class WorkplaceGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = WorkPlace
        fields = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = '__all__'


class ProjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = ('project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name')


class ProjectUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyProjects
        fields = ('id', 'project_title', 'description', 'skills', 'start_date', 'end_date', 'team_size', 'client_name')


class ProjectGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyProjects
        fields = ('id',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = '__all__'


class LanguagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = ('name', 'read', 'write', 'speak')


class LanguageUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyLanguage
        fields = ('id', 'name', 'read', 'write', 'speak')


class LanguageGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyLanguage
        fields = ('id',)


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = '__all__'


class InterestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = ('interact_code',)


class InterestUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyInterest
        fields = ('id', 'interact_code',)


class InterestGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = MyInterest
        fields = ('id',)


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'


class SocialLinksPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ('name', 'unique_id')


class SocialLinksUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = SocialLinks
        fields = ('id', 'name', 'unique_id')


class SocialLinksGetDeleteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)

    class Meta:
        model = SocialLinks
        fields = ('id',)
