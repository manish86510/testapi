from django.urls import path,re_path
from management.views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from management import views as user_views
from posts import urls as posts_urls

urlpatterns = [
   path('', dashboard, name="dashboard"),
   path('batch/', batch, name="batch"),
   path('trainer/', trainer, name="trainer"),
   path('finance/', finance, name="finance"),
   path('session/', session, name="session"),
   path('precources/', precources, name="precources"),
   path('recording/', recording, name="recordin"),
   path('notification/', notification, name="notification"),
   path('loginuser/', loginuser, name="loginuser"),
   path('registeruser/', registeruser, name="registeruser"),
   path('logoutuser/', logoutuser, name="logoutuser"),
   

   path('creatbatch/', creatbatch, name='creatbatch'),
   path('activ/<int:id>/', activ, name='activ'),
   path('noactiv/<int:id>/', noactiv, name='noactiv'),
   path('editbatch/<int:id>/', editbatch, name='editbatch'),
   path('batchshow/<int:id>/', batchshow, name='batchshow'),
   path('createuser/', createuser, name='createuser'),
   path('creategroup/', creategroup, name='creategroup'),
   path('fronbatcdeleteuser/<str:id>/', fronbatcdeleteuser, name='fronbatcdeleteuser'),
   path('relative/', relative, name='relative'),
   path('createsession/', createsession, name='createsession'),
   path('editsession/<int:id>/', editsession, name='editsession'),
   path('sessionactive/<int:id>/', sessionactive, name='sessionactive'),
   path('sessiondeactive/<int:id>/', sessiondeactive, name='sessiondeactive'),
   path('createtraner/', createtraner, name='createtraner'),
   path('languages/', languages, name='languages'),
   path('traneractive/<int:id>/', traneractive, name='traneractive'),
   path('trainerdeactive/<int:id>/', trainerdeactive, name='trainerdeactive'),
   path('news/', news, name='news'),
   path('posts/', include('Posts_urls'))


]

