from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_city import CitySerializer


class CitySwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["City"],
            operation_summary="Add City",
            operation_description="Creates city field",
            request_body=CitySerializer,
            responses={200: CitySerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["City"],
            operation_summary="Delete City",
            operation_description="Creates city field",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["City"],
            operation_summary="Update City",
            operation_description="Creates city field",
            request_body=CitySerializer,
            responses={200: CitySerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["City"],
            operation_summary="List City",
            operation_description="Creates city field",
            responses={200: CitySerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["City"],
            operation_summary="Get City",
            operation_description="Creates city field",
            responses={200: CitySerializer}
        )
        return doc
