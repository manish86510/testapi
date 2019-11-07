from django.shortcuts import render
#from pip import logger
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import random
import requests
import json
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm)
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework import permissions, generics
from django.core.mail import send_mail
from django.conf import settings
from .models import *
import string
#from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


'''@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest Swagger')
    return Response(generator.get_schema(request=request))'''


class HelloView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CreateUserView(generics.ListAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, format=None):
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(25))
        serializer_class = UserSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            user = User.objects.latest('id')
            user.verify_mail_code = code
            user.save()
            subject = 'Thank you for registering to our site'
            message = "Click here http://127.0.0.1:8000/verify_mail/"+ code +" to verify your email id."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            if send_mail(subject, message, email_from, recipient_list):
                return Response("Please verify your mail", status=HTTP_200_OK)
            else:
                return Response("Verification Mail not sent! ", status=HTTP_200_OK)
        else:
            return Response("Wrong Entry!", status=HTTP_200_OK)


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        a=request.get_host()
        if form.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.get(email=email):
                form.save(request=request)
                return JsonResponse({'message': 'Check your E-mail'})
            else:
                return JsonResponse({'message': 'Invalid E-mail'})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        jdata = {
            "username": str(username),
            "password": password
        }
        #curl = request._current_scheme_host
        curl = "http://127.0.0.1:8000/api/token"
        token_content = requests.post(curl, json=jdata)
        token_content_json = token_content.json()
        #logger.info(type(token_content))
        if token_content.status_code == 200:
            try:
                user = User.objects.get(username=username, is_mail_verified=True)
            except:
                return JsonResponse({'message': 'Invalid login'})
            user_data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'about': user.about if user.about else '',
                'email': user.email,
                'avatar': str(user.avatar) if str(user.avatar) else '',
                'address': user.address if user.address else '',
                'skill': user.skills if user.skills else '',
            }
            return JsonResponse({'user_data': user_data, 'token': token_content_json})
        else:
            return JsonResponse({'message': 'Invalid login'})



def update_profile(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST.get('email', ''))
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.salutation = request.POST.get('salutation', '')
            user.about = request.POST.get('about', '')
            user.avatar = request.POST.get('avatar', '')
            user.cover_picture = request.POST.get('cover_picture', '')
            user.posts_count = request.POST.get('posts_count', '')
            user.followers_count = request.POST.get('followers_count', '')
            user.following_count = request.POST.get('following_count', '')
            user.skills = request.POST.get('skills', '')
            user.address = request.POST.get('address', '')
            user.enlarge_url = request.POST.get('enlarge_url', '')
            user.date_of_birth = request.POST.get('date_of_birth', '')
            user.birth_place = request.POST.get('birth_place', '')
            user.gender = request.POST.get('gender', '')
            user.save()
        except:
            return JsonResponse({'failed': "Profile not updated"})
        return JsonResponse({'success': "Profile updated successfully!"})


@api_view(["GET"])
@permission_classes((AllowAny,))
def verifyMail(self, code):
    try:
        User.objects.filter(verify_mail_code=code).update(is_mail_verified=True)
    except:
        return Response("Link has been expired", status=HTTP_200_OK)
    return Response("Mail verified successfully!", status=HTTP_200_OK)

@permission_classes((IsAuthenticated,))
def education(self):
    if self.method == 'POST':
        try:
            education = Education.objects.create(user=self.POST.get('email', ''))
            education.school_college_name = self.POST.get('school_college_name', '')
            education.description = self.POST.get('session_from', '')
            education.session_to = self.POST.get('session_to', '')
            education.attended_for = self.POST.get('attended_for', '')
            education.save()
        except:
            return Response("Education data not updated", status=HTTP_200_OK)
    else:
        education = Education.objects.get(user=self.POST.get('email', ''))
        return Response({'education': education}, status=HTTP_200_OK)
