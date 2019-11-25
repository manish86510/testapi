from rest_framework import viewsets, permissions
from .models import *
from .serializers.user import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .serializers.user_city import CitySerializer
from .serializers.user_education import EducationSerializer
from .serializers.user_my_followers import FollowerSerializer
from .serializers.user_my_interest import InterestSerializer
from .serializers.user_my_languages import LanguageSerializer
from .serializers.user_my_places import PlaceSerializer
from .serializers.user_my_projects import ProjectsSerializer
from .serializers.user_my_skills import SkillSerializer
from .serializers.user_social_links import SocialLinksSerializer
from .serializers.user_workplace import WorkplaceSerializer
from .swagger.user import UserSwaggerDoc
from .swagger.user_city import CitySwagger
from .swagger.user_education import EducationSwagger
from .swagger.user_my_followers import FollowerSwagger
from .swagger.user_my_interest import InterestSwagger
from .swagger.user_my_languages import LanguageSwagger
from .swagger.user_my_places import PlaceSwagger
from .swagger.user_my_projects import ProjectSwagger
from .swagger.user_my_skills import SkillSwagger
from .swagger.user_social_links import SocialLinkSwagger
from .swagger.user_workplace import WorkplaceSwagger
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK
from django.conf import settings
import string, random


@method_decorator(name='create', decorator=UserSwaggerDoc.create())
@method_decorator(name='list', decorator=UserSwaggerDoc.list())
@method_decorator(name='destroy', decorator=UserSwaggerDoc.delete())
@method_decorator(name='update', decorator=UserSwaggerDoc.update())
@method_decorator(name='retrieve', decorator=UserSwaggerDoc.retrieve())
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.AllowAny, ]
    serializer_action_class = {
        'list': UserSerializer,
        'create': UserCreateSerializer,
        'update': UserUpdateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_class[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def create(self, request):
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for _ in range(25))
        serializer_class = UserCreateSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            user = User.objects.latest('id')
            user.verify_mail_code = code
            user.save()
            subject = 'Thank you for registering to our site'
            message = "Click here http://energe.do.viewyoursite.net/verify_mail/" + code + " to verify your email id."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            if send_mail(subject, message, email_from, recipient_list):
                return Response("Please verify your mail", status=HTTP_200_OK)
            else:
                return Response("Verification Mail not sent!", status=HTTP_200_OK)
        else:
            return Response(serializer_class.errors)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def verifyMail(code):
    try:
        User.objects.filter(verify_mail_code=code).update(is_mail_verified=True)
    except:
        return Response("Link has been expired", status=HTTP_200_OK)
    return Response("Mail verified successfully!", status=HTTP_200_OK)


@method_decorator(name='create', decorator=CitySwagger.create())
@method_decorator(name='list', decorator=CitySwagger.list())
@method_decorator(name='destroy', decorator=CitySwagger.delete())
@method_decorator(name='update', decorator=CitySwagger.update())
@method_decorator(name='retrieve', decorator=CitySwagger.retrieve())
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = City.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(CityViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=EducationSwagger.create())
@method_decorator(name='list', decorator=EducationSwagger.list())
@method_decorator(name='destroy', decorator=EducationSwagger.delete())
@method_decorator(name='update', decorator=EducationSwagger.update())
@method_decorator(name='retrieve', decorator=EducationSwagger.retrieve())
class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = Education.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(EducationViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=FollowerSwagger.create())
@method_decorator(name='list', decorator=FollowerSwagger.list())
@method_decorator(name='destroy', decorator=FollowerSwagger.delete())
@method_decorator(name='update', decorator=FollowerSwagger.update())
@method_decorator(name='retrieve', decorator=FollowerSwagger.retrieve())
class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = Followers.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(FollowerViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=InterestSwagger.create())
@method_decorator(name='list', decorator=InterestSwagger.list())
@method_decorator(name='destroy', decorator=InterestSwagger.delete())
@method_decorator(name='update', decorator=InterestSwagger.update())
@method_decorator(name='retrieve', decorator=InterestSwagger.retrieve())
class InterestViewSet(viewsets.ModelViewSet):
    serializer_class = InterestSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyInterest.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(InterestViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=LanguageSwagger.create())
@method_decorator(name='list', decorator=LanguageSwagger.list())
@method_decorator(name='destroy', decorator=LanguageSwagger.delete())
@method_decorator(name='update', decorator=LanguageSwagger.update())
@method_decorator(name='retrieve', decorator=LanguageSwagger.retrieve())
class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyLanguage.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(LanguageViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=PlaceSwagger.create())
@method_decorator(name='list', decorator=PlaceSwagger.list())
@method_decorator(name='destroy', decorator=PlaceSwagger.delete())
@method_decorator(name='update', decorator=PlaceSwagger.update())
@method_decorator(name='retrieve', decorator=PlaceSwagger.retrieve())
class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyPlaces.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PlaceViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=ProjectSwagger.create())
@method_decorator(name='list', decorator=ProjectSwagger.list())
@method_decorator(name='destroy', decorator=ProjectSwagger.delete())
@method_decorator(name='update', decorator=ProjectSwagger.update())
@method_decorator(name='retrieve', decorator=ProjectSwagger.retrieve())
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyProjects.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(ProjectViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=SkillSwagger.create())
@method_decorator(name='list', decorator=SkillSwagger.list())
@method_decorator(name='destroy', decorator=SkillSwagger.delete())
@method_decorator(name='update', decorator=SkillSwagger.update())
@method_decorator(name='retrieve', decorator=SkillSwagger.retrieve())
class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = MySkills.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(SkillViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=SocialLinkSwagger.create())
@method_decorator(name='list', decorator=SocialLinkSwagger.list())
@method_decorator(name='destroy', decorator=SocialLinkSwagger.delete())
@method_decorator(name='update', decorator=SocialLinkSwagger.update())
@method_decorator(name='retrieve', decorator=SocialLinkSwagger.retrieve())
class SocialLinkViewSet(viewsets.ModelViewSet):
    serializer_class = SocialLinksSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = SocialLinks.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(SocialLinkViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=WorkplaceSwagger.create())
@method_decorator(name='list', decorator=WorkplaceSwagger.list())
@method_decorator(name='destroy', decorator=WorkplaceSwagger.delete())
@method_decorator(name='update', decorator=WorkplaceSwagger.update())
@method_decorator(name='retrieve', decorator=WorkplaceSwagger.retrieve())
class WorkplaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkplaceSerializer

    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = WorkPlace.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(WorkplaceViewSet, self).list(request, *args, **kwargs)
