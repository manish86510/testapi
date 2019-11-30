from drf_yasg.utils import swagger_auto_schema
from Posts.serializers.get_full_post_info import GetFullPostInfoSerializer


class GetFullPostSwagger:

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["Get Posts"],
            operation_summary="List Post",
            operation_description="List posts using the details provided by the user",
            responses={200: GetFullPostInfoSerializer(many=True)}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["Get Posts"],
            operation_summary="Get Post",
            operation_description="Get post using the details provided by the user",
            responses={200: GetFullPostInfoSerializer}
        )
        return doc
