from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_media import PostMediaSerializer, PostMediaCreateSerializer


class PostMediaSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Media"],
            operation_summary="Creates a New Media",
            operation_description="Creates Media using the details provided by the user",
            request_body=PostMediaCreateSerializer,
            responses={'200': PostMediaSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Media"],
            operation_summary="Delete Media",
            operation_description="Delete Media using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Media"],
            operation_summary="Update Media",
            operation_description="Update Media using the details provided by the user",
            request_body=PostMediaCreateSerializer,
            responses={'200': PostMediaSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Media"],
            operation_summary="List Media",
            operation_description="Listing Media",
            responses={200: PostMediaSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Media"],
            operation_summary="Get Media",
            operation_description="Get Media using the details provided by the user",
            responses={200: PostMediaSerializer}
        )
        return doc
