from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.post_likes import PostLikeSerializer, PostLikeCreateSerializer


class PostLikeSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["Post Like"],
            operation_summary="Creates a New Like",
            operation_description="Creates Like using the details provided by the user",
            request_body=PostLikeCreateSerializer,
            responses={'200': PostLikeSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["Post Like"],
            operation_summary="Delete Like",
            operation_description="Delete Like using the details provided by the user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["Post Like"],
            operation_summary="Update Like",
            operation_description="Update Like using the details provided by the user",
            request_body=PostLikeCreateSerializer,
            responses={'200': PostLikeSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Post Like"],
            operation_summary="List Like",
            operation_description="List Like using the details provided by the user",
            responses={200: PostLikeSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Post Like"],
            operation_summary="Get Like",
            operation_description="Get Like using the details provided by the user",
            responses={200: PostLikeSerializer}
        )
        return doc
