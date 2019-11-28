from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.skill import SkillCreateSerializer


class SkillSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Skill"],
            operation_summary="Add Skills",
            operation_description="Adds skills to global skill table",
            request_body=SkillCreateSerializer,
            responses={200: SkillCreateSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Skill"],
            operation_summary="Delete Skill",
            operation_description="Deletes skill from global skill table",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Skill"],
            operation_summary="Update Skill",
            operation_description="Updates skill in the global skill table",
            request_body=SkillCreateSerializer,
            responses={200: SkillCreateSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Skill"],
            operation_summary="Get All Skills",
            operation_description="List all skills present in skills table",
            responses={200: SkillCreateSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Skill"],
            operation_summary="Get Skill by ID",
            operation_description="Retrieve individual skill by ID",
            responses={200: SkillCreateSerializer}
        )
        return doc
