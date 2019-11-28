from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_interest import MyInterestSerializer


class MyInterestSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Interest"],
            operation_summary="Add User Interest",
            operation_description="Adds a user interest by the user",
            request_body=MyInterestSerializer,
            responses={200: MyInterestSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Interest"],
            operation_summary="Delete User Interest",
            operation_description="Delete a user interest by ID",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Interest"],
            operation_summary="Update User Interest",
            operation_description="Updates a user interest by the user",
            request_body=MyInterestSerializer,
            responses={200: MyInterestSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Interest"],
            operation_summary="List User Interest",
            operation_description="List all user interests",
            responses={200: MyInterestSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Interest"],
            operation_summary="Retrieve User Interest",
            operation_description="Retrieve a user interest by ID",
            responses={200: MyInterestSerializer}
        )
        return doc
