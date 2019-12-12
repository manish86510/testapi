from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import BasePermission
from rest_framework.parsers import MultiPartParser, FormParser

from .models import *
from .serializers.user import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserCustomFieldSerializer
from .serializers.user_city import CitySerializer
from .serializers.user_education import EducationSerializer
from .serializers.user_my_followers import FollowerSerializer, FollowerCreateSerializer
from .serializers.user_my_interest import MyInterestSerializer
from .serializers.user_my_languages import MyLanguageSerializer
from .serializers.user_my_places import PlaceSerializer
from .serializers.user_my_projects import ProjectsSerializer
from .serializers.user_my_skills import MySkillSerializer
from .serializers.user_social_links import SocialLinksSerializer
from .serializers.user_workplace import WorkplaceSerializer
from .serializers.interest import InterestSerializer
from .serializers.language import LanguageSerializer
from .serializers.skill import SkillCreateSerializer

from .swagger.user import UserSwaggerDoc, RecommendedUserListSwaggerDoc
from .swagger.user_city import CitySwagger
from .swagger.user_education import EducationSwagger
from .swagger.user_my_followers import FollowerSwagger, FriendsListSwagger
from .swagger.user_my_interest import MyInterestSwagger
from .swagger.user_my_languages import MyLanguageSwagger
from .swagger.user_my_places import PlaceSwagger
from .swagger.user_my_projects import ProjectSwagger
from .swagger.user_my_skills import MySkillSwagger
from .swagger.user_social_links import SocialLinkSwagger
from .swagger.user_workplace import WorkplaceSwagger
from .swagger.interest import InterestSwagger
from .swagger.language import LanguageSwagger
from .swagger.skill import SkillSwagger
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_408_REQUEST_TIMEOUT,
)
from django.conf import settings
import string, random
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import redirect


class AllowCreateUser(BasePermission):
    def has_permission(self, request, view):
        if (request.method in ['POST'] or
                request.user and
                request.user.is_authenticated):
            return True
        return False


from rest_framework.parsers import FileUploadParser


@method_decorator(name='retrieve', decorator=FriendsListSwagger.retrieve())
@method_decorator(name='list', decorator=FriendsListSwagger.list())
class FriendListViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = FollowerSerializer

    http_method_names = ['get']

    def get_queryset(self):
        queryset = Followers.objects.filter(user=self.request.user.id, is_confirmed=True)
        return queryset


@method_decorator(name='put', decorator=UserSwaggerDoc.update())
class UserUpdateViewSet(APIView):
    http_method_names = ['put']

    # parser_classes = (FileUploadParser,)

    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_obj = UserSerializer(request.user)
            return Response(user_obj.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@method_decorator(name='create', decorator=UserSwaggerDoc.create())
@method_decorator(name='list', decorator=UserSwaggerDoc.list())
@method_decorator(name='destroy', decorator=UserSwaggerDoc.delete())
# @method_decorator(name='update', decorator=UserSwaggerDoc.update())
@method_decorator(name='retrieve', decorator=UserSwaggerDoc.retrieve())
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'delete']
    serializer_action_class = {
        'list': UserSerializer,
        'create': UserCreateSerializer,
        'update': UserUpdateSerializer,
    }
    permission_classes = [AllowCreateUser]

    def get_queryset(self, **kwargs):
        queryset = User.objects.filter(id=self.kwargs.get('pk'), is_active=True)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = User.objects.get(id=self.request.user.id, is_active=True)
        serializer = UserCustomFieldSerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)

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
            user = serializer_class.save()
            user.verify_mail_code = code
            user.save()
            subject = 'Thank you for registering to our site'
            message = "Click here http://energeapi.do.viewyoursite.net/user/verify_mail/" + code + "to verify your " \
                                                                                                   "email id. "
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            if send_mail(subject, message, email_from, recipient_list):
                return Response("Please verify your mail", status=HTTP_200_OK)
            else:
                return Response("Verification Mail not sent!", status=HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        query = User.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def verifyMail(self, code):
    try:
        user_obj = User.objects.filter(verify_mail_code=code).update(is_mail_verified=True)
    except:
        return Response("Link has been expired", status=HTTP_400_BAD_REQUEST)
    return redirect('http://energe.do.viewyoursite.net/verify_mail/{}'.format(code))


@method_decorator(name='create', decorator=CitySwagger.create())
@method_decorator(name='list', decorator=CitySwagger.list())
@method_decorator(name='destroy', decorator=CitySwagger.delete())
@method_decorator(name='update', decorator=CitySwagger.update())
@method_decorator(name='retrieve', decorator=CitySwagger.retrieve())
class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = City.objects.all()
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()


@method_decorator(name='create', decorator=EducationSwagger.create())
@method_decorator(name='list', decorator=EducationSwagger.list())
@method_decorator(name='destroy', decorator=EducationSwagger.delete())
@method_decorator(name='update', decorator=EducationSwagger.update())
@method_decorator(name='retrieve', decorator=EducationSwagger.retrieve())
class MyEducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = Education.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = Education.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=FollowerSwagger.create())
@method_decorator(name='list', decorator=FollowerSwagger.list())
@method_decorator(name='destroy', decorator=FollowerSwagger.delete())
@method_decorator(name='update', decorator=FollowerSwagger.update())
@method_decorator(name='retrieve', decorator=FollowerSwagger.retrieve())
class MyFollowerViewSet(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = Followers.objects.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = FollowerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            follower = User.objects.get(pk=request.data.get('follower'))
            serializer.save(follower=follower, user=self.request.user)
            return Response({"message": "ok"}, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        query = Followers.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=MyInterestSwagger.create())
@method_decorator(name='list', decorator=MyInterestSwagger.list())
@method_decorator(name='destroy', decorator=MyInterestSwagger.delete())
@method_decorator(name='update', decorator=MyInterestSwagger.update())
@method_decorator(name='retrieve', decorator=MyInterestSwagger.retrieve())
class MyInterestViewSet(viewsets.ModelViewSet):
    serializer_class = MyInterestSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyInterest.objects.all()  # filter(user=self.request.user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = MyInterest.objects.filter(user=self.request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = MyInterest.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=MyLanguageSwagger.create())
@method_decorator(name='list', decorator=MyLanguageSwagger.list())
@method_decorator(name='destroy', decorator=MyLanguageSwagger.delete())
@method_decorator(name='update', decorator=MyLanguageSwagger.update())
@method_decorator(name='retrieve', decorator=MyLanguageSwagger.retrieve())
class MyLanguageViewSet(viewsets.ModelViewSet):
    serializer_class = MyLanguageSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyLanguage.objects.all()  # filter(user=self.request.user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = MyLanguage.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=PlaceSwagger.create())
@method_decorator(name='list', decorator=PlaceSwagger.list())
@method_decorator(name='destroy', decorator=PlaceSwagger.delete())
@method_decorator(name='update', decorator=PlaceSwagger.update())
@method_decorator(name='retrieve', decorator=PlaceSwagger.retrieve())
class MyPlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyPlaces.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = MyPlaces.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=ProjectSwagger.create())
@method_decorator(name='list', decorator=ProjectSwagger.list())
@method_decorator(name='destroy', decorator=ProjectSwagger.delete())
@method_decorator(name='update', decorator=ProjectSwagger.update())
@method_decorator(name='retrieve', decorator=ProjectSwagger.retrieve())
class MyProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = MyProjects.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = MyProjects.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=MySkillSwagger.create())
@method_decorator(name='list', decorator=MySkillSwagger.list())
@method_decorator(name='destroy', decorator=MySkillSwagger.delete())
@method_decorator(name='update', decorator=MySkillSwagger.update())
@method_decorator(name='retrieve', decorator=MySkillSwagger.retrieve())
class MySkillViewSet(viewsets.ModelViewSet):
    serializer_class = MySkillSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = MySkills.objects.all()  # filter(user=self.request.user.id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=self.request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = MySkills.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=SocialLinkSwagger.create())
@method_decorator(name='list', decorator=SocialLinkSwagger.list())
@method_decorator(name='destroy', decorator=SocialLinkSwagger.delete())
@method_decorator(name='update', decorator=SocialLinkSwagger.update())
@method_decorator(name='retrieve', decorator=SocialLinkSwagger.retrieve())
class SocialLinkViewSet(viewsets.ModelViewSet):
    serializer_class = SocialLinksSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = SocialLinks.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = SocialLinks.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=WorkplaceSwagger.create())
@method_decorator(name='list', decorator=WorkplaceSwagger.list())
@method_decorator(name='destroy', decorator=WorkplaceSwagger.delete())
@method_decorator(name='update', decorator=WorkplaceSwagger.update())
@method_decorator(name='retrieve', decorator=WorkplaceSwagger.retrieve())
class WorkplaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkplaceSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = WorkPlace.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = WorkPlace.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=InterestSwagger.create())
@method_decorator(name='list', decorator=InterestSwagger.list())
@method_decorator(name='destroy', decorator=InterestSwagger.delete())
@method_decorator(name='update', decorator=InterestSwagger.update())
@method_decorator(name='retrieve', decorator=InterestSwagger.retrieve())
class InterestViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = InterestSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        if self.request.GET.get('querystring'):
            queryset = Interests.objects.filter(interest__istartswith=self.request.GET.get('search'))
        else:
            queryset = Interests.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        query = Interests.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=SkillSwagger.create())
@method_decorator(name='list', decorator=SkillSwagger.list())
@method_decorator(name='destroy', decorator=SkillSwagger.delete())
@method_decorator(name='update', decorator=SkillSwagger.update())
@method_decorator(name='retrieve', decorator=SkillSwagger.retrieve())
class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = SkillCreateSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        if self.request.GET.get('search'):
            queryset = Skills.objects.filter(skill__istartswith=self.request.GET.get('search'))
        else:
            queryset = Skills.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        query = Skills.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=LanguageSwagger.create())
@method_decorator(name='list', decorator=LanguageSwagger.list())
@method_decorator(name='destroy', decorator=LanguageSwagger.delete())
@method_decorator(name='update', decorator=LanguageSwagger.update())
@method_decorator(name='retrieve', decorator=LanguageSwagger.retrieve())
class LanguageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = LanguageSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        if self.request.GET.get('search'):
            queryset = Languages.objects.filter(language__istartswith=self.request.GET.get('search'))
        else:
            queryset = Languages.objects.all()
        return queryset

    def destroy(self, request, *args, **kwargs):
        query = Languages.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='list', decorator=RecommendedUserListSwaggerDoc.list())
class RecommendedViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer

    http_method_names = ['get']

    def get_queryset(self):
        follower_obj = Followers.objects.filter(user=self.request.user.id).values_list('follower')
        queryset = User.objects.filter(is_active=True).exclude(pk__in=follower_obj).exclude(pk=self.request.user.id)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     follower_obj = Followers.objects.filter(user=request.user.id).values_list('follower')
    #     queryset = User.objects.filter(is_active=True).exclude(pk__in=follower_obj).exclude(pk=request.user.id)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, status=HTTP_200_OK)
