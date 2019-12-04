from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user import UserSerializer, UserCreateSerializer, UserUpdateSerializer


class UserSwaggerDoc:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["User"],
            operation_summary="Creates a New User",
            operation_description="Creates a new user using `username`, `email`, and `password`",
            request_body=UserCreateSerializer,
            responses={'200': UserSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["User"],
            operation_summary="Deletes a user",
            operation_description="Deletes all user data",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["User"],
            operation_summary="Updates User Info",
            operation_description="Updates user information of an existing user",
            request_body=UserUpdateSerializer,
            responses={'200': UserSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["User"],
            operation_summary="List Users",
            operation_description="List registered users",
            responses={200: UserSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["User"],
            operation_summary="Get User",
            operation_description="Get user information by id",
            responses={200: UserSerializer}
        )
        return doc
