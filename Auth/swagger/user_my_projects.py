from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_projects import ProjectsSerializer, ProjectsCreateSerializer


class ProjectSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Projects"],
            operation_summary="Adds a User Project",
            operation_description="Adds information about a user projects",
            request_body=ProjectsCreateSerializer,
            responses={200: ProjectsSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Projects"],
            operation_summary="Delete a User Project",
            operation_description="Delete information about a user projects",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Projects"],
            operation_summary="Updates a User Project",
            operation_description="Updates information about a user projects",
            request_body=ProjectsCreateSerializer,
            responses={200: ProjectsSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Projects"],
            operation_summary="Lists All User Project",
            operation_description="Lists all information about a user's projects",
            responses={200: ProjectsSerializer}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Projects"],
            operation_summary="Retrieve a User Project",
            operation_description="Retrieve information about a user project",
            responses={200: ProjectsSerializer}
        )
        return doc
