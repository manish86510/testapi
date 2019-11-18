from django.shortcuts import render
# from pip import logger
from drf_yasg import openapi
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
from rest_framework import permissions, generics, status
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from Posts.models import *
import string
# import requests
from datetime import datetime
from rest_framework import serializers
from rest_framework.decorators import parser_classes, action
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser

# from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


'''@api_view()
@permission_classes((AllowAny, ))
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest Swagger')
    return Response(generator.get_schema(request=request))'''

'''@swagger_auto_schema(
    tags=["Posts Media"],
    operation_summary="Create New Media Entry",
    operation_description="Creates a new media entry when any new media is uploaded for a post",
    responses={
        200: PostMediaSerializer,
    }
)'''


class GetById(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def get(self, request):
        data = request.data
        print(data)


class CreateUserView(APIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]

    @swagger_auto_schema(
        tags=["New User"],
        operation_summary="Creates a New User",
        operation_description="Create a new user by providing credentials such as `username`,"
                              + " `email id` and `password`",
        request_body=UserSerializer,
        responses={
            200: UserSerializer,
        }
    )
    def post(self, request, format=None):
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(25))
        serializer_class = UserSerializer(data=request.data)
        # import pdb
        # pdb.set_trace()
        if serializer_class.is_valid():
            serializer_class.save()
            user = User.objects.latest('id')
            user.verify_mail_code = code
            user.save()
            subject = 'Thank you for registering to our site'
            message = "Click here https://energe.do.viewyoursite.net/verify_mail/" + code + " to verify your email id."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            if send_mail(subject, message, email_from, recipient_list):
                return Response("Please verify your mail", status=HTTP_200_OK)
            else:
                return Response("Verification Mail not sent! ", status=HTTP_200_OK)
        else:
            return Response("Wrong Entry!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["New User"],
        operation_summary="Get all User Table",
        operation_description="Get user table as output in response with information about all the users",
        query_serializer=UserSerializer,
        responses={
            200: UserSerializer,
        }
    )
    def get(self, instance):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"Users": serializer.data})


@swagger_auto_schema(
    tags=["Password Reset"],
    operation_summary="Password Reset Method",
    operation_description="Allows a user to reset the password of the account.",
    query_serializer=UserSerializer,
    responses={
        200: UserSerializer,
    }
)
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        a = request.get_host()
        if form.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.get(email=email):
                form.save(request=request)
                return JsonResponse({'message': 'Check your E-mail'})
            else:
                return JsonResponse({'message': 'Invalid E-mail'})


# @api_view(["POST"])
# @permission_classes((AllowAny,))
# @swagger_auto_schema(
#     tags=["Login"],
#     operation_summary="Login API",
#     operation_description="User can login from here",
#     query_serializer=UserSerializer,
#     responses={
#         200: UserSerializer,
#     }
# )
# def login(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     jdata = {
#         "username": str(username),
#         "password": password
#     }
#     # curl = request._current_scheme_host
#     curl = "http://127.0.0.1:8000/api/token"
#     token_content = requests.post(curl, json=jdata)
#     token_content_json = token_content.json()
#     # logger.info(type(token_content))
#     if token_content.status_code == 200:
#         try:
#             user = User.objects.get(username=username, is_mail_verified=True)
#         except:
#             return JsonResponse({'message': 'Invalid login'})
#         user_data = {
#             'id': user.id,
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'about': user.about if user.about else '',
#             'email': user.email,
#             'avatar': str(user.avatar) if str(user.avatar) else '',
#             'address': user.address if user.address else '',
#             'skill': user.skills if user.skills else '',
#         }
#         return JsonResponse({'user_data': user_data, 'token': token_content_json})
#     else:
#         return JsonResponse({'message': 'Invalid login'})

class UpdateProfile(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["Update Profile"],
        operation_summary="Updates a User Profile",
        operation_description="Update user profile details",
        request_body=UserUpdateSerializer,
        responses={
            200: UserUpdateSerializer,
        }
    )
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

class MyEducation(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]


    @swagger_auto_schema(
        tags=["User Education"],
        operation_summary="Add Education Details",
        operation_description="Add education details of any user",
        request_body=EducationPostSerializer,
        responses={
            200: EducationSerializer,
        }
    )
    def post(self, request):
        pk = request.user.id
        education = EducationPostSerializer(data=request.data)
        if education.is_valid():
            education.save(user_id=pk)
            return Response("Your Education details inserted!", status=HTTP_200_OK)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Education"],
        operation_summary="Update Education Details",
        operation_description="Update education details of any user",
        request_body=EducationUpdateSerializer,
        responses={
            200: EducationSerializer,
        }
    )
    def put(self, request):
        import pdb
        pdb.set_trace()
        pk = request.data.get('id')
        ui = request.user.id
        saved_education = get_object_or_404(Education.objects.all(), id=pk, user=ui)
        serializer = EducationUpdateSerializer(instance=saved_education, data=request.data, partial=True)
        # import pdb
        # pdb.set_trace()
        if serializer.is_valid(raise_exception=True):
            education_saved = serializer.save()
        return Response({"success": "Education '{}' updated successfully".format(education_saved.school_college_name)})

    @swagger_auto_schema(
        tags=["User Education"],
        operation_summary="Delete Education Details",
        operation_description="Delete education details of any user",
        request_body=EducationSerializer,
        responses={
            200: EducationSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        education = get_object_or_404(Education.objects.all(), pk=pk)
        education.delete()
        return Response({"message": "Education with id `{}` has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(
        tags=["User Education"],
        operation_summary="Get Education Details",
        operation_description="Get education details of current user",
        # query_serializer=EducationSerializer,
        responses={
            200: EducationSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        education = Education.objects.filter(user=ui)
        serializer = EducationSerializer(education, many=True)
        return Response({"education": serializer.data})


class Places(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Places"],
        operation_summary="Add My Place Details",
        operation_description="Add My Place details of any user",
        query_serializer=PlaceSerializer,
        responses={
            200: PlaceSerializer,
        }
    )
    def post(self, request):
        # pk = int(request.POST.get('user'))
        pk = request.user
        place = PlaceSerializer(data=request.data)
        if place.is_valid():
            place.save(user=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Place details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Places"],
        operation_summary="Update My Place Details",
        operation_description="Update My Place details of any user",
        request_body=PlaceSerializer,
        responses={
            200: PlaceSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_places = get_object_or_404(MyPlaces.objects.all(), pk=pk)
        serializer = PlaceSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "MyPlace '{}' updated successfully".format(places_saved.place_name)})

    @swagger_auto_schema(
        tags=["User Places"],
        operation_summary="Delete My Place Details",
        operation_description="Delete My Place details of current user",
        request_body=PlaceSerializer,
        responses={
            200: PlaceSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(MyPlaces.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "MyPlace with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Places"],
    #     operation_summary="Get My Place Details",
    #     operation_description="Get My Place details of all users",
    #     query_serializer=PlaceSerializer,
    #     responses={
    #         200: PlaceSerializer,
    #     }
    # )
    # def get(self, instance):
    #     place = MyPlaces.objects.all()
    #     serializer = PlaceSerializer(place, many=True)
    #     return Response({"MyPlace": serializer.data})

    @swagger_auto_schema(
        tags=["User Places"],
        operation_summary="Get My Place Details",
        operation_description="Get My Place details of current user",
        # query_serializer=PlaceSerializer,
        responses={
            200: PlaceSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        place = MyPlaces.objects.filter(user=ui)
        serializer = PlaceSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})


class Language(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Languages"],
        operation_summary="Add Language Details",
        operation_description="Add Language details of current user",
        request_body=LanguageSerializer,
        responses={
            200: LanguageSerializer,
        }
    )
    def post(self, request):
        # pk = int(request.POST.get('user'))
        pk = request.user.id
        # import pdb
        # pdb.set_trace()
        language = LanguageSerializer(data=request.data)
        if language.is_valid():
            language.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Language details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Languages"],
        operation_summary="Update Language Details",
        operation_description="Update education details of current user",
        request_body=LanguageSerializer,
        responses={
            200: LanguageSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_language = get_object_or_404(MyLanguage.objects.all(), pk=pk)
        serializer = LanguageSerializer(instance=saved_language, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            language_saved = serializer.save()
        return Response({"success": "Language '{}' updated successfully".format(language_saved.name)})

    @swagger_auto_schema(
        tags=["User Languages"],
        operation_summary="Delete Language Details",
        operation_description="Delete education details of current user",
        request_body=LanguageSerializer,
        responses={
            200: LanguageSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        education = get_object_or_404(MyLanguage.objects.all(), pk=pk)
        education.delete()
        return Response({"message": "Language with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Languages"],
    #     operation_summary="Get Language Details",
    #     operation_description="Get education details of all users",
    #     query_serializer=LanguageSerializer,
    #     responses={
    #         200: LanguageSerializer,
    #     }
    # )
    # def get(self, instance):
    #     place = MyLanguage.objects.all()
    #     serializer = LanguageSerializer(place, many=True)
    #     return Response({"Language": serializer.data})

    @swagger_auto_schema(
        tags=["User Languages"],
        operation_summary="Get Language Details",
        operation_description="Get education details of current user",
        # query_serializer=LanguageSerializer,
        responses={
            200: LanguageSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        place = MyLanguage.objects.filter(user=ui)
        serializer = LanguageSerializer(place, many=True)
        return Response({"Language": serializer.data})


class MyWorkplace(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Workplace"],
        operation_summary="Add Workplace Details",
        operation_description="Add My Work Place details of any user",
        request_body=WorkplaceSerializer,
        responses={
            200: WorkplaceSerializer,
        }
    )
    def post(self, request):
        pk = request.user.id
        work = WorkplaceSerializer(data=request.data)
        if work.is_valid():
            work.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Work Place details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Workplace"],
        operation_summary="Update Workplace Details",
        operation_description="Update Work Place details of any user",
        request_body=WorkplaceSerializer,
        responses={
            200: WorkplaceSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_workplace = get_object_or_404(WorkPlace.objects.all(), pk=pk)
        serializer = WorkplaceSerializer(instance=saved_workplace, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            workplace_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(workplace_saved.name)})

    @swagger_auto_schema(
        tags=["User Workplace"],
        operation_summary="Delete Workplace Details",
        operation_description="Delete Work Place details of any user",
        request_body=WorkplaceSerializer,
        responses={
            200: WorkplaceSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        workplace = get_object_or_404(WorkPlace.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "Work Place with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Workplace"],
    #     operation_summary="Get Workplace Details",
    #     operation_description="Get Work Place details of all users",
    #     query_serializer=WorkplaceSerializer,
    #     responses={
    #         200: WorkplaceSerializer,
    #     }
    # )
    # def get(self, instance):
    #     place = WorkPlace.objects.all()
    #     serializer = WorkplaceSerializer(place, many=True)
    #     return Response({"WorkPlace": serializer.data})

    @swagger_auto_schema(
        tags=["User Workplace"],
        operation_summary="Get Workplace Details",
        operation_description="Get Work Place details of currrent user",
        # query_serializer=WorkplaceSerializer,
        responses={
            200: WorkplaceSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        place = WorkPlace.objects.filter(user=ui)
        serializer = WorkplaceSerializer(place, many=True)
        return Response({"WorkPlace": serializer.data})


class Projects(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Projects"],
        operation_summary="Add Projects Details",
        operation_description="Add My Project details of any user",
        request_body=ProjectSerializer,
        responses={
            200: ProjectSerializer,
        }
    )
    def post(self, request):
        pk = request.user
        project = ProjectSerializer(data=request.data)
        if project.is_valid():
            project.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Project details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Projects"],
        operation_summary="Update Projects Details",
        operation_description="Update My Project details of any user",
        request_body=ProjectSerializer,
        responses={
            200: ProjectSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_project = get_object_or_404(MyProjects.objects.all(), pk=pk)
        serializer = ProjectSerializer(instance=saved_project, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(project_saved.project_title)})

    @swagger_auto_schema(
        tags=["User Projects"],
        operation_summary="Delete Projects Details",
        operation_description="Delete My Project details of any user",
        request_body=ProjectSerializer,
        responses={
            200: ProjectSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        workplace = get_object_or_404(MyProjects.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "Work Place with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Projects"],
    #     operation_summary="Get Projects Details",
    #     operation_description="Get My Project details of all users",
    #     query_serializer=ProjectSerializer,
    #     responses={
    #         200: ProjectSerializer,
    #     }
    # )
    # def get(self, instance):
    #     project = MyProjects.objects.all()
    #     serializer = ProjectSerializer(project, many=True)
    #     return Response({"My Projects": serializer.data})

    @swagger_auto_schema(
        tags=["User Projects"],
        operation_summary="Get Projects Details",
        operation_description="Get My Project details of current user",
        # query_serializer=ProjectSerializer,
        responses={
            200: ProjectSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        project = MyProjects.objects.filter(user=ui)
        serializer = ProjectSerializer(project, many=True)
        return Response({"My Projects": serializer.data})


class Social(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Social Media"],
        operation_summary="Add Social Media Details",
        operation_dscription="Add Social Media details of any user",
        request_body=SocialLinksSerializer,
        responses={
            200: SocialLinksSerializer,
        }
    )
    def post(self, request):
        pk = request.user.id
        social = SocialLinksSerializer(data=request.data)
        if social.is_valid():
            social.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Social details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Social Media"],
        operation_summary="Update Social Media Details",
        operation_description="Update Social Media details of any user",
        request_body=SocialLinksSerializer,
        responses={
            200: SocialLinksSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_data = get_object_or_404(SocialLinks.objects.all(), pk=pk)
        serializer = ProjectSerializer(instance=saved_data, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            data_saved = serializer.save()
        return Response({"success": "Work Place '{}' updated successfully".format(data_saved.name)})

    @swagger_auto_schema(
        tags=["User Social Media"],
        operation_summary="Delete Social Media Details",
        operation_description="Delete Social Media details of any user",
        request_body=SocialLinksSerializer,
        responses={
            200: SocialLinksSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        social = get_object_or_404(SocialLinks.objects.all(), pk=pk)
        social.delete()
        return Response({"message": "Social Links with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Social Media"],
    #     operation_summary="Get Social Media Details",
    #     operation_description="Get Social Media details of all users",
    #     query_serializer=SocialLinksSerializer,
    #     responses={
    #         200: SocialLinksSerializer,
    #     }
    # )
    # def get(self, instance):
    #     project = SocialLinks.objects.all()
    #     serializer = SocialLinksSerializer(project, many=True)
    #     return Response({"SocialLinks": serializer.data})

    @swagger_auto_schema(
        tags=["User Social Media"],
        operation_summary="Get Social Media Details",
        operation_description="Get Social Media details of current user",
        # query_serializer=SocialLinksSerializer,
        responses={
            200: SocialLinksSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        project = SocialLinks.objects.filter(user=ui)
        serializer = SocialLinksSerializer(project, many=True)
        return Response({"SocialLinks": serializer.data})


class Interest(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @swagger_auto_schema(
        tags=["User Interests"],
        operation_summary="Add User Interests Details",
        operation_description="Add My Interest details of any user",
        request_body=InterestSerializer,
        responses={
            200: InterestSerializer,
        }
    )
    def post(self, request):
        pk = request.user
        project = InterestSerializer(data=request.data)
        if project.is_valid():
            project.save(user_id=pk)
        else:
            return Response("Data not stored, Please try again!", status=HTTP_200_OK)
        return Response("Your Interest details inserted!", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["User Interests"],
        operation_summary="Update User Interests Details",
        operation_description="Update My Interest details of any user",
        request_body=InterestSerializer,
        responses={
            200: InterestSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_project = get_object_or_404(MyInterest.objects.all(), pk=pk)
        serializer = InterestSerializer(instance=saved_project, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
        return Response({"success": "Interest '{}' updated successfully".format(project_saved.project_title)})

    @swagger_auto_schema(
        tags=["User Interests"],
        operation_summary="Delete User Interests Details",
        operation_description="Delete My Interest details of any user",
        request_body=InterestSerializer,
        responses={
            200: InterestSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        workplace = get_object_or_404(MyProjects.objects.all(), pk=pk)
        workplace.delete()
        return Response({"message": "My Interest with id `{}` has been deleted.".format(pk)}, status=204)

    # @swagger_auto_schema(
    #     tags=["User Interests"],
    #     operation_summary="Get User Interests Details",
    #     operation_description="Get My Interest details of all users",
    #     query_serializer=InterestSerializer,
    #     responses={
    #         200: InterestSerializer,
    #     }
    # )
    # def get(self, instance):
    #     project = MyInterest.objects.all()
    #     serializer = InterestSerializer(project, many=True)
    #     return Response({"My Interest": serializer.data})

    @swagger_auto_schema(
        tags=["User Interests"],
        operation_summary="Get User Interests Details",
        operation_description="Get My Interest details of current user",
        # query_serializer=InterestSerializer,
        responses={
            200: InterestSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        project = MyInterest.objects.filter(user=ui)
        serializer = InterestSerializer(project, many=True)
        return Response({"My Interest": serializer.data})


@api_view(["GET"])
@permission_classes((AllowAny,))
# @swagger_auto_schema(
#     tags=["Verify Email"],
#     operation_summary="Verify Mail",
#     operation_description="Updates the verify mail entry within the user table if the email is verified by the user.",
#     # query_serializer=UserSerializer,
#     # responses={
#     #     200: UserSerializer,
#     # }
# )
def verifyMail(self, code):
    try:
        User.objects.filter(verify_mail_code=code).update(is_mail_verified=True)
    except:
        return Response("Link has been expired", status=HTTP_200_OK)
    return Response("Mail verified successfully!", status=HTTP_200_OK)
