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
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = Education
        fields = ('school_college_name', 'description', 'session_from', 'session_to', 'attended_for')


class EducationUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, read_only=False)
    class Meta:
        model = Education
        fields = ('id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for')
        write_only_fields = ('id', 'school_college_name', 'description', 'session_from', 'session_to', 'attended_for')
        # read_only_fields = ('id', )
    # def get(self, validated_data):
    #     import pdb
    #     pdb.set_trace()
    #     model = Education.objects.get(id=validated_data['id'])
    #     education = model.create(validated_data)
    #     education.save()
    #     return education


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = '__all__'


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProjects
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyLanguage
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInterest
        fields = '__all__'


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = '__all__'
