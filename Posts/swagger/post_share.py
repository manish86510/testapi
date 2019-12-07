from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_share import PostShareSerializer, PostShareCreateSerializer


class PostShareSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Creates a New Share",
            operation_description="Creates Share using the details provided by the user",
            request_body=PostShareCreateSerializer,
            responses={'200': PostShareSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Delete Share",
            operation_description="Delete Share using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Update Share",
            operation_description="Update Share using the details provided by the user",
            request_body=PostShareCreateSerializer,
            responses={'200': PostShareSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="List Share",
            operation_description="List Share using the details provided by the user",
            responses={200: PostShareSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Share"],
            operation_summary="Get Share",
            operation_description="get Share using the details provided by the user",
            responses={200: PostShareSerializer}
        )
        return doc
