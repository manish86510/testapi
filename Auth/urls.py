from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello'),
    path('register', CreateUserView.as_view(), name='register'),
    path('verify_mail/<str:code>', verifyMail, name='verify_mail'),
    path('update_profile', UpdateProfile.as_view(), name='update_profile'),
    path('education', Education.as_view(), name='education'),
    path('my_places', Places.as_view(), name='my_places'),
    path('my_projects', MyProjects.as_view(), name='my_projects'),
    path('work_place', Workplace.as_view(), name='work_place'),
    path('my_language', MyLanguage.as_view(), name='my_language'),
]