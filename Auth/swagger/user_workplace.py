from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_workplace import WorkplaceSerializer


class WorkplaceSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Workplace"],
            operation_summary="Add User Workplace",
            operation_description="Adds information about user workplace",
            request_body=WorkplaceSerializer,
            responses={200: WorkplaceSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Workplace"],
            operation_summary="Delete User Workplace",
            operation_description="Delete information about user workplace",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Workplace"],
            operation_summary="Update User Workplace",
            operation_description="Update information about user workplace",
            request_body=WorkplaceSerializer,
            responses={200: WorkplaceSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Workplace"],
            operation_summary="List All User Workplaces",
            operation_description="Lists information about all the user's workplaces",
            responses={200: WorkplaceSerializer}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Workplace"],
            operation_summary="Retrieve User Workplace",
            operation_description="Retrieve information about user workplace",
            responses={200: WorkplaceSerializer}
        )
        return doc
