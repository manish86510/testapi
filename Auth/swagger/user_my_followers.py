from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_followers import FollowerSerializer, FollowerCreateSerializer


class FollowerSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="Add a Follower",
            operation_description="Add a follower to the current user",
            request_body=FollowerCreateSerializer,
            responses={200: FollowerSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="Delete Follower",
            operation_description="Delete follower to the current user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="Update Follower",
            operation_description="Update follower to the current user",
            request_body=FollowerCreateSerializer,
            responses={200: FollowerSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="List Follower",
            operation_description="List followers",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="Get Follower",
            operation_description="Get follower to the current user",
            responses={200: FollowerSerializer}
        )
        return doc
