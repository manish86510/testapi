from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_followers import FollowerSerializer, FollowerCreateSerializer


class FollowerSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=['Follow'],
            operation_summary="Follow a person",
            operation_description="Follow a person",
            request_body=FollowerCreateSerializer,
            responses={200: FollowerSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=['Follow'],
            operation_summary="Delete Following",
            operation_description="Delete follower to the current user",
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="List of follower",
            operation_description="List of followers",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=['Followers'],
            operation_summary="Get details of follower",
            operation_description="Get details of follower",
            responses={200: FollowerSerializer(many=False)}
        )
        return doc



class FollowingSwagger:
    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=['Following'],
            operation_summary="List of following",
            operation_description="List of following",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=['Following'],
            operation_summary="Get following user details",
            operation_description="Get following user details",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc


class FriendsListSwagger:
    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=['Friends List'],
            operation_summary="List Friends",
            operation_description="List Friends to tha current user",
            responses={200: FollowerSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=['Friends List'],
            operation_summary="Get Friends",
            operation_description="Get Friends to the current user",
            responses={200: FollowerSerializer}
        )
        return doc