from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_education import EducationSerializer, EducationCreateSerializer


class EducationSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Education"],
            operation_summary="Add User's Education Information",
            operation_description="Adds education information for the user",
            request_body=EducationCreateSerializer,
            responses={200: EducationSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Education"],
            operation_summary="Delete User's Education Information",
            operation_description="Adds education information for the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Education"],
            operation_summary="Update User's Education Information",
            operation_description="Adds education information for the user",
            request_body=EducationCreateSerializer,
            responses={200: EducationSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Education"],
            operation_summary="Get User's All Education Information",
            operation_description="Adds education information for the user",
            responses={200: EducationSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Education"],
            operation_summary="Get User's Education Information by ID",
            operation_description="Adds education information for the user",
            responses={200: EducationSerializer}
        )
        return doc
