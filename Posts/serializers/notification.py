from rest_framework import serializers
# from .user_field import CurrentUserID
from Posts.models import *
from .post_tag import *
from .post_likes import *
from .post_comments import *
from .post_media import *
from .post_share import *
from Auth.serializers.user import UserFollowerDetailSerializer


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('notification_type', 'notification_url', 'notification_status', 'notification_message', 'read_date',
                  'sender_id', 'user_id')


class NotificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('notification_type', 'notification_url', 'notification_status', 'notification_message', 'read_date',
                  'sender_id', 'user_id')
