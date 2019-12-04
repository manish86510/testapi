from rest_framework import serializers
from Auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'address', 'avatar', 'cover_picture', 'email')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
        queryset = ''

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('salutation', 'first_name', 'last_name', 'about', 'avatar',
                  'cover_picture', 'skills', 'address', 'enlarge_url', 'date_of_birth',
                  'birth_place', 'gender')
