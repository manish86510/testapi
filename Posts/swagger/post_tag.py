from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_tag import PostTagSerializer


class PostTagSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Tag"],
            operation_summary="Creates a New Tag",
            operation_description="Creates tag using the details provided by the user",
            request_body=PostTagSerializer,
            responses={'200': PostTagSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Tag"],
            operation_summary="Delete Tag",
            operation_description="Creates tag using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Tag"],
            operation_summary="Update Tag",
            operation_description="Creates tag using the details provided by the user",
            request_body=PostTagSerializer,
            responses={'200': PostTagSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Tag"],
            operation_summary="List Tag",
            operation_description="Creates tag using the details provided by the user",
            responses={200: PostTagSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Tag"],
            operation_summary="Get Tag",
            operation_description="Creates tag using the details provided by the user",
            responses={200: PostTagSerializer}
        )
        return doc
