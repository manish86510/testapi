from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_share import PostShareSerializer, PostShareCreateSerializer


class PostShareSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Creates a New Post",
            operation_description="Creates post using the details provided by the user",
            request_body=PostShareCreateSerializer,
            responses={'200': PostShareSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Delete Post",
            operation_description="Creates post using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Update Post",
            operation_description="Creates post using the details provided by the user",
            request_body=PostShareCreateSerializer,
            responses={'200': PostShareSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="List Post",
            operation_description="Creates post using the details provided by the user",
            responses={200: PostShareSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Get Post",
            operation_description="Creates post using the details provided by the user",
            responses={200: PostShareSerializer}
        )
        return doc
