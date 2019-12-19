from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.notification import *


class NotificationSwaggerDoc:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Notifications"],
            operation_summary="Creates a New Notifications",
            operation_description="Creates Notifications using the details provided by the user",
            request_body=NotificationCreateSerializer,
            responses={'200': NotificationSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Notifications"],
            operation_summary="Delete Notifications",
            operation_description="Creates Notifications using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Notifications"],
            operation_summary="Update Notifications",
            operation_description="Creates Notifications using the details provided by the user",
            request_body=NotificationCreateSerializer,
            responses={'200': NotificationSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Notifications"],
            operation_summary="List Notifications",
            operation_description="Creates Notifications using the details provided by the user",
            responses={200: NotificationSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Notifications"],
            operation_summary="Get Notifications",
            operation_description="Creates Notifications using the details provided by the user",
            responses={200: NotificationSerializer}
        )
        return doc
