from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.interest import InterestSerializer


class InterestSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Interest"],
            operation_summary="Add Interests",
            operation_description="Adds Interest to global Interest table",
            request_body=InterestSerializer,
            responses={200: InterestSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Interest"],
            operation_summary="Delete Interest",
            operation_description="Deletes Interest from global Interest table",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Interest"],
            operation_summary="Update Interest",
            operation_description="Updates Interest in the global Interest table",
            request_body=InterestSerializer,
            responses={200: InterestSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Interest"],
            operation_summary="Get All Interests",
            operation_description="List all Interests present in Interests table",
            responses={200: InterestSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Interest"],
            operation_summary="Get Interest by ID",
            operation_description="Retrieve individual Interest by ID",
            responses={200: InterestSerializer}
        )
        return doc
