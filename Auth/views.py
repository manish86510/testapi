from django.shortcuts import render
#from pip import logger
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
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
from datetime import datetime
from rest_framework import serializers
#from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


'''@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest Swagger')
    return Response(generator.get_schema(request=request))'''


class GetById(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class CreateUserView(APIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]

    @swagger_auto_schema(operation_description="Create a new user", query_serializer=UserSerializer, responses={200: UserSerializer})
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


@api_view(["POST"])
@permission_classes((AllowAny,))
@swagger_auto_schema(operation_description="User can login from here", query_serializer=UserSerializer, responses={200: UserSerializer})
def login(request):
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
            'id': user.id,
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


class UpdateProfile(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Update user profile details", query_serializer=UserSerializer, responses={200: UserSerializer})
    def post(self, request):
        try:
            user = User.objects.get(email=request.POST.get('email', ''))
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.salutation = request.POST.get('salutation', '')
            user.about = request.POST.get('about', '')
            user.avatar = request.POST.get('avatar', '')
            user.cover_picture = request.POST.get('cover_picture', '')
            user.posts_count = int(request.POST.get('posts_count', ''))
            user.followers_count = int(request.POST.get('followers_count', ''))
            user.following_count = int(request.POST.get('following_count', ''))
            user.skills = request.POST.get('skills', '')
            user.address = request.POST.get('address', '')
            user.enlarge_url = request.POST.get('enlarge_url', '')
            user.date_of_birth = datetime.strptime(request.POST.get('date_of_birth', ''), "%Y-%m-%d").date()
            user.birth_place = request.POST.get('birth_place', '')
            user.gender = request.POST.get('gender', '')
            user.save()
        except:
            return Response({'failed': "Profile not updated"})
        return Response({'success': "Profile updated successfully!"})


@api_view(["GET"])
@permission_classes((AllowAny,))
def verifyMail(self, code):
    try:
        User.objects.filter(verify_mail_code=code).update(is_mail_verified=True)
    except:
        return Response("Link has been expired", status=HTTP_200_OK)
    return Response("Mail verified successfully!", status=HTTP_200_OK)


class MyEducation(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add education details of any user", query_serializer=EducationSerializer, responses={200: EducationSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        education = EducationSerializer(data=request.data)
        if education.is_valid():
            education.save(user_id=pk)
            return Response("Your Education details inserted!", status=HTTP_200_OK)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update education details of any user", query_serializer=EducationSerializer, responses={200: EducationSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_education = get_object_or_404(Education.objects.all(), pk=pk)
        serializer = EducationSerializer(instance=saved_education, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            education_saved = serializer.save()
        return Response({"success": "Education '{}' updated successfully".format(education_saved.school_college_name)})


    def delete(self, request):
        pk = int(request.POST.get('user'))
        education = get_object_or_404(Education.objects.all(), pk=pk)
        education.delete()
        return Response({"message": "Education with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        education = Education.objects.all()
        serializer = EducationSerializer(education, many=True)
        return Response({"education": serializer.data})


class Places(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add My Place details of any user", query_serializer=PlaceSerializer, responses={200: PlaceSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        place = PlaceSerializer(data=request.data)
        if place.is_valid():
            place.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Place details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update My Place details of any user", query_serializer=PlaceSerializer, responses={200: PlaceSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_places = get_object_or_404(MyPlaces.objects.all(), pk=pk)
        serializer = PlaceSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "MyPlace '{}' updated successfully".format(places_saved.place_name)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        place = get_object_or_404(MyPlaces.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "MyPlace with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = MyPlaces.objects.all()
        serializer = PlaceSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})

class Language(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add Language details of any user", query_serializer=LanguageSerializer, responses={200: LanguageSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        language = LanguageSerializer(data=request.data)
        if language.is_valid():
            language.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Language details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update education details of any user", query_serializer=LanguageSerializer, responses={200: LanguageSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_language = get_object_or_404(MyLanguage.objects.all(), pk=pk)
        serializer = LanguageSerializer(instance=saved_language, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            language_saved = serializer.save()
        return Response({"success": "Language '{}' updated successfully".format(language_saved.name)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        education = get_object_or_404(MyLanguage.objects.all(), pk=pk)
        education.delete()
        return Response({"message": "Language with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = MyLanguage.objects.all()
        serializer = LanguageSerializer(place, many=True)
        return Response({"Language": serializer.data})


class MyWorkplace(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add My Work Place details of any user", query_serializer=WorkplaceSerializer, responses={200: WorkplaceSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        work = WorkplaceSerializer(data=request.data)
        if work.is_valid():
            work.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Work Place details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update Work Place details of any user", query_serializer=WorkplaceSerializer, responses={200: WorkplaceSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_workplace = get_object_or_404(WorkPlace.objects.all(), pk=pk)
        serializer = WorkplaceSerializer(instance=saved_workplace, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            workplace_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(workplace_saved.name)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        workplace = get_object_or_404(WorkPlace.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "Work Place with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = WorkPlace.objects.all()
        serializer = WorkplaceSerializer(place, many=True)
        return Response({"WorkPlace": serializer.data})


class Projects(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add My Project details of any user", query_serializer=ProjectSerializer, responses={200: ProjectSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        project = ProjectSerializer(data=request.data)
        if project.is_valid():
            project.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Project details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update My Project details of any user", query_serializer=ProjectSerializer, responses={200: ProjectSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_project = get_object_or_404(MyProjects.objects.all(), pk=pk)
        serializer = ProjectSerializer(instance=saved_project, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(project_saved.project_title)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        workplace = get_object_or_404(MyProjects.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "Work Place with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        project = MyProjects.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response({"My Projects": serializer.data})


class Social(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_dscription="Add Social Media details of any user", query_serializer=SocialLinksSerializer, responses={200: SocialLinksSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        social = SocialLinksSerializer(data=request.data)
        if social.is_valid():
            social.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Social details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update education details of any user", query_serializer=SocialLinksSerializer, responses={200: SocialLinksSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_data = get_object_or_404(SocialLinks.objects.all(), pk=pk)
        serializer = ProjectSerializer(instance=saved_data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            data_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(data_saved.name)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        social = get_object_or_404(SocialLinks.objects.all(), pk=pk)
        social.delete()
        return Response({"message": "Social Links with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        project = SocialLinks.objects.all()
        serializer = SocialLinksSerializer(project, many=True)
        return Response({"SocialLinks": serializer.data})


class Interest(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(operation_description="Add My Interest details of any user", query_serializer=InterestSerializer, responses={200: InterestSerializer})
    def post(self, request):
        pk = int(request.POST.get('user'))
        project = InterestSerializer(data=request.data)
        if project.is_valid():
            project.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Interest details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update My Interest details of any user", query_serializer=InterestSerializer, responses={200: InterestSerializer})
    def put(self, request):
        pk = int(request.POST.get('user'))
        saved_project = get_object_or_404(MyInterest.objects.all(), pk=pk)
        serializer = InterestSerializer(instance=saved_project, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
        return Response({"success": "Interest '{}' updated successfully".format(project_saved.project_title)})

    def delete(self, request):
        pk = int(request.POST.get('user'))
        workplace = get_object_or_404(MyProjects.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "My Interest with id `{}` has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        project = MyInterest.objects.all()
        serializer = InterestSerializer(project, many=True)
        return Response({"My Interest": serializer.data})