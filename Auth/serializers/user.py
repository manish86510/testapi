from rest_framework import serializers
from Auth.models import User


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'address', 'avatar', 'cover_picture', 'email',
                  'enlarge_url', 'about', 'followers_count', 'following_count')

    def get_followers_count(self, obj):
        if not obj.followers_count:
            obj.followers_count = 0
        return obj.followers_count

    def get_following_count(self, obj):
        if not obj.following_count:
            obj.following_count = 0
        return obj.following_count


class UserCustomFieldSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'address', 'avatar', 'cover_picture', 'email',
                  'enlarge_url', 'about')

    def get_first_name(self, obj):
        if obj.first_name:
            return obj.first_name
        return ''

    def get_last_name(self, obj):
        if obj.last_name:
            return obj.last_name
        return ''


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
        write_only_fields = ('password',)

    def create(self, validated_data):
        queryset = ''

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, read_only=True)

    # avatar = serializers.CharField(help_text="Upload Image ImageField",required=False)

    class Meta:
        model = User
        fields = ('username', 'avatar', 'first_name', 'last_name', 'about', 'enlarge_url','address','cover_picture')


class UserFollowerDetailSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'username', 'avatar', 'followers_count')

    def get_followers_count(self, obj):
        if not obj.followers_count:
            obj.followers_count = 0
        return obj.followers_count
