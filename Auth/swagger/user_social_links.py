from drf_yasg.utils import swagger_auto_schema
from Auth.serializers.user_social_links import SocialLinksSerializer, SocialLinksCreateSerializer


class SocialLinkSwagger:

    @staticmethod
    def create():
        doc = swagger_auto_schema(
            tags=["My Social Links"],
            operation_summary="Add Social Links",
            operation_description="Add social links for a user",
            request_body=SocialLinksCreateSerializer,
            responses={200: SocialLinksSerializer}
        )
        return doc

    @staticmethod
    def delete():
        doc = swagger_auto_schema(
            tags=["My Social Links"],
            operation_summary="Delete Social Links",
            operation_description="Delete social links for a user",
        )
        return doc

    @staticmethod
    def update():
        doc = swagger_auto_schema(
            tags=["My Social Links"],
            operation_summary="Updates Social Links",
            operation_description="Updates social links for a user",
            request_body=SocialLinksCreateSerializer,
            responses={200: SocialLinksSerializer}
        )
        return doc

    @staticmethod
    def list():
        doc = swagger_auto_schema(
            tags=["My Social Links"],
            operation_summary="List Social Links",
            operation_description="List all social links for a user",
            responses={200: SocialLinksSerializer}
        )
        return doc

    @staticmethod
    def retrieve():
        doc = swagger_auto_schema(
            tags=["My Social Links"],
            operation_summary="Retrieve Social Links",
            operation_description="Retrieve social links for a user",
            responses={200: SocialLinksSerializer}
        )
        return doc
