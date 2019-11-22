from rest_framework import viewsets, permissions
from .models import *
from .serializers.user import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .serializers.user_city import CitySerializer
from .swagger.user import UserSwaggerDoc
from .swagger.user_city import CitySwagger
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
            message = "Click here http://127.0.0.1:8000/verify_mail/" + code + " to verify your email id."
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
def verifyMail(self, code):
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
