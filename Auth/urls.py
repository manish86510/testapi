from django.urls import path, include
from .views import *


urlpatterns = [
    # path('register', CreateUserView.as_view(), name='register'),
    # path('resend', ResendEmail.as_view(), name='resend_email'),
    # path('verify_mail/<str:code>', verifyMail, name='verify_mail'),
    # path('update_profile', UpdateProfile.as_view(), name='update_profile'),
    # path('education', MyEducation.as_view(), name='education'),
    # path('my_places', Places.as_view(), name='my_places'),
    # path('my_projects', Projects.as_view(), name='my_projects'),
    # path('work_place', MyWorkplace.as_view(), name='work_place'),
    # path('my_language', Language.as_view(), name='my_language'),
    # path('my_interest', Interest.as_view(), name='my_interest'),
    # path('my_social', Social.as_view(), name='my_social'),
    # path('get_by_id/', include([
    #     path('education', GetEducationById.as_view(), name='education_by_id'),
    #     path('places', GetPlacesById.as_view(), name='places_by_id'),
    #     path('projects', GetProjectsById.as_view(), name='projects_by_id'),
    #     path('workplace', GetWorkplaceById.as_view(), name='workplace_by_id'),
    #     path('language', GetLanguagesById.as_view(), name='languages_by_id'),
    #     path('interest', GetInterestsById.as_view(), name='interests_by_id'),
    #     path('social', GetSocialMediaById.as_view(), name='social_by_id'),
    # ])),
    # path('get_all/', include([
    #     path('user', GetUserAll.as_view(), name='user_all'),
    #     path('education', GetEducationAll.as_view(), name='education_all'),
    #     path('places', GetPlacesAll.as_view(), name='places_all'),
    #     path('projects', GetProjectsAll.as_view(), name='projects_all'),
    #     path('workplace', GetWorkplaceAll.as_view(), name='workplace_all'),
    #     path('language', GetLanguagesAll.as_view(), name='languages_all'),
    #     path('interest', GetInterestsAll.as_view(), name='interests_all'),
    #     path('social', GetSocialMediaAll.as_view(), name='social_all'),
    # ])),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

