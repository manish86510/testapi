from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #path('hello', GetById.as_view(), name='hello'),
    path('register', CreateUserView.as_view(), name='register'),
    path('verify_mail/<str:code>', verifyMail, name='verify_mail'),
    path('update_profile', UpdateProfile.as_view(), name='update_profile'),
    path('education', MyEducation.as_view(), name='education'),
    path('my_places', Places.as_view(), name='my_places'),
    path('my_projects', Projects.as_view(), name='my_projects'),
    path('work_place', MyWorkplace.as_view(), name='work_place'),
    path('my_language', Language.as_view(), name='my_language'),
    path('my_interest', Interest.as_view(), name='my_interest'),
    path('my_social', Social.as_view(), name='my_social'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)