from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_followers import FollowerSerializer


class FollowerSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=['My Follower'],
            operation_summary="Adds a Follower",
            operation_description="Adds a follower to the current user",
            request_body=FollowerSerializer,
            responses={200: FollowerSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=['My Follower'],
            operation_summary="Adds a Follower",
            operation_description="Adds a follower to the current user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=['My Follower'],
            operation_summary="Adds a Follower",
            operation_description="Adds a follower to the current user",
            request_body=FollowerSerializer,
            responses={200: FollowerSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=['My Follower'],
            operation_summary="Adds a Follower",
            operation_description="Adds a follower to the current user",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=['My Follower'],
            operation_summary="Adds a Follower",
            operation_description="Adds a follower to the current user",
            responses={200: FollowerSerializer}
        )
        return doc
