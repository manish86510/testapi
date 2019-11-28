from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_my_skills import MySkillSerializer


class MySkillSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Skills"],
            operation_summary="Adds User Skill",
            operation_description="Adds My skill information for the user",
            request_body=MySkillSerializer,
            responses={200: MySkillSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Skills"],
            operation_summary="Delete User Skill",
            operation_description="Deletes My skill information for the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Skills"],
            operation_summary="Updates User Skill",
            operation_description="Updates My skill information for the user",
            request_body=MySkillSerializer,
            responses={200: MySkillSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Skills"],
            operation_summary="Lists User Skills",
            operation_description="List all My skill information for the user",
            responses={200: MySkillSerializer}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Skills"],
            operation_summary="Retrieve User Skill",
            operation_description="Retrieve My skill information for the user",
            responses={200: MySkillSerializer}
        )
        return doc

