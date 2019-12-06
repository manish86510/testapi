from rest_framework import serializers
from Auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'address', 'avatar', 'cover_picture', 'email',
                  'enlarge_url', 'about')


class UserCustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'address', 'avatar', 'cover_picture', 'email',
                  'enlarge_url', 'about')


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
        fields = ('username', 'first_name', 'last_name', 'about', 'enlarge_url',)


class UserFollowerDetailSerializer(serializers.ModelSerializer):
    # followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'avatar', 'followers_count')

    # def get_followers_count(self, obj):
    #     if not obj.followers_count:
    #         obj.followers_count = 0
    #     return obj
