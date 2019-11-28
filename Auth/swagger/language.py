from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.language import LanguageSerializer


class LanguageSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Language"],
            operation_summary="Add Languages",
            operation_description="Adds Languages to global Language table",
            request_body=LanguageSerializer,
            responses={200: LanguageSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Language"],
            operation_summary="Delete Language",
            operation_description="Deletes Language from global Language table",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Language"],
            operation_summary="Update Language",
            operation_description="Updates Language in the global Language table",
            request_body=LanguageSerializer,
            responses={200: LanguageSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Language"],
            operation_summary="Get All Languages",
            operation_description="List all Languages present in Languages table",
            responses={200: LanguageSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Language"],
            operation_summary="Get Language by ID",
            operation_description="Retrieve individual Language by ID",
            responses={200: LanguageSerializer}
        )
        return doc
