from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post import *


class PostSwaggerDoc:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Posts"],
            operation_summary="Creates a New Post",
            operation_description="Creates post using the details provided by the user",
            request_body=PostCreateSerializer,
            responses={'200': PostSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Posts"],
            operation_summary="Delete Post",
            operation_description="Creates post using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Posts"],
            operation_summary="Update Post",
            operation_description="Creates post using the details provided by the user",
            request_body=PostCreateSerializer,
            responses={'200': PostSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Posts"],
            operation_summary="List Post",
            operation_description="Creates post using the details provided by the user",
            responses={200: PostAllDetailSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Posts"],
            operation_summary="Get Post",
            operation_description="Creates post using the details provided by the user",
            responses={200: PostAllDetailSerializer}
        )
        return doc


class HotTopicSwaggerDoc:
    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Hot Topic"],
            operation_summary="Get Hot Topic",
            operation_description="Got Latest hot topic in post",
            responses={200: PostAllDetailSerializer}
        )
        return doc