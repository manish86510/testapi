from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('hello', HelloView.as_view(), name='hello'),
    path('register', CreateUserView.as_view(), name='register'),
    path('verify_mail/<str:code>', verifyMail, name='verify_mail'),
    path('update_profile', csrf_exempt(update_profile), name='update_profile'),
]
