from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_places import PlaceSerializer, PlaceCreateSerializer


class PlaceSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Places"],
            operation_summary="Add User Place",
            operation_description="Add a my place for the user",
            request_body=PlaceCreateSerializer,
            responses={200: PlaceSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Places"],
            operation_summary="Deletes User Place",
            operation_description="Deletes a my place for the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Places"],
            operation_summary="Updates User Place",
            operation_description="Updates a my place for the user",
            request_body=PlaceCreateSerializer,
            responses={200: PlaceSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Places"],
            operation_summary="List All User Places",
            operation_description="List all my place entries for the user",
            responses={200: PlaceSerializer}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Places"],
            operation_summary="Retrieve User Place",
            operation_description="Retrieve a my place for the user",
            responses={200: PlaceSerializer}
        )
        return doc
