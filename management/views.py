from ast import Pass, Return
from datetime import time
from re import U
from django.contrib import messages
import re
from tokenize import group
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import  render, redirect
from django.contrib.auth import login,logout, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from Auth.models import Admin_user, User
from django.contrib.auth.forms import UserCreationForm
import ipdb
# import Posts
from datetime import datetime

from Auth.models import *

def home(request):
    return render(request, 'managment/index.html')

def dashboard(request):
    try:
        request.session['email']
        test = None
        return render(request, 'managment/dashboard.html')
    except:
        return render(request, 'managment/login.html')
     
def batch(request):
    try:
        request.session['email']
        test = None

        batch=Batch.objects.all()
        return render(request, 'managment/batch.html',{'batch':batch})
    except:
        return render(request, 'managment/login.html')

def news(request):
    try:
        request.session['email']
        test = None
        return render(request, 'managment/news.html')
    except:
        return render(request, 'managment/login.html')        

    
def trainer(request):  
    try:
        request.session['email']
        test = None
        traner=Trainer.objects.all()
        return render(request, 'managment/trainer.html',{'traner':traner})
    except:
        return render(request, 'managment/login.html')
      

def finance(request):
    if 'email' in request.session:
        return render(request, 'managment/trainer.html')
    else:
        return render(request, 'managment/login.html')
    

def session(request):
    try:
        event=Event.objects.all()
        request.session['email']
        test = None
        return render(request, 'managment/session.html',{'event':event})
    except:
        return render(request, 'managment/login.html')
    

def precources(request):
    try:
        request.session['email']
        test = None
        return render(request, 'managment/precource.html')
    except:
        return render(request, 'managment/login.html')
    

def recording(request):
    try:
        request.session['email']
        test = None
        return render(request, 'managment/recording.html')
    except:
        return render(request, 'managment/login.html')
    

def notification(request):
    try:
        request.session['email']
        test = None
        return render(request, 'managment/notification.html')
    except:
        return render(request, 'managment/login.html')
    


def loginuser(request):
    if request.method=="POST":
       
        login = None
        try:
            login = User.objects.get(email=request.POST['email'], password=request.POST['password'],is_active=1)
            request.session['email'] =request.POST['email']
            return redirect('dashboard')
        except:
            return redirect('loginuser')
    return render(request, 'managment/login.html')        


def registeruser(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User()
        user.email=email
        user.username=username
        user.password=password
        user.is_active=1
        user.save()
        return redirect('loginuser')
    return render(request, 'managment/registation.html')   

def logoutuser(request):
    request.session.flush()
    messages.info(request, "You have successfully logged out.") 
    return redirect("loginuser")

def creatbatch(request):
    if request.session['email']:
        test = None
    else:
        return render(request, 'login.html')
    if request.method=="POST": 
        user=User.objects.get(email=request.session['email'])    
        name=request.POST['createbatch']
        batch=Batch()
        batch.name=name
        batch.created_by=user
        batch.is_active=0
        batch.save()
        return redirect('batch')
    return render(request,'managment/createbatch.html')

def activ(request,id):
    

    batch=Batch.objects.get(id=id)
    batch.is_active=1
    batch.save()
    return redirect('batch')

def noactiv(request,id):
    batch=Batch.objects.get(id=id)
    batch.is_active=0
    batch.save()
    return redirect('batch')


def createuser(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        salutation=request.POST['salutation']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        image=request.POST['image']
        coverphoto=request.POST['coverphoto']
        about=request.POST['about']
        skills=request.POST['skills']
        address=request.POST['address']
        url=request.POST['url']
        date_of_birth=request.POST['date_of_birth']
        birth_place=request.POST['birth_place']
        gender=request.POST['gender']
        user=User()
        user.username=username
        user.email=email
        user.password=password
        user.salutation=salutation
        user.first_name=first_name
        user.last_name=last_name
        user.about=about
        user.avatar=image
        user.cover_picture=coverphoto
        user.skills=skills
        user.enlarge_url=url
        user.address=address
        user.date_of_birth=date_of_birth
        user.birth_place=birth_place
        user.gender=gender
        user.save()
        return redirect('dashboard')
    return render(request,'managment/createuser.html')



def rest(request, id):
    if request.session['email']:
        pass
    return render(request,'managment/createuser.html')



def creategroup(request):

    if request.method=="GET":
        user=User.objects.all()
        batch=Batch.objects.all()
        return render(request,'managment/creategroup.html',{'user':user,'batch':batch})
    elif request.method=="POST":  
        email=request.POST['usere']
        user1=User.objects.get(email=email)
        batch=Batch.objects.get(name=request.POST['batch'])
        groupuser=GroupUser()
        groupuser.group=batch
        groupuser.user=user1
        groupuser.save()
        return redirect('batch') 


def batchshow(request,id):
    data = GroupUser.objects.filter(group=id)
    return render(request, 'managment/batchshow.html',{'data':data})


"""
1.brand195
2.woofunds
3.flypoter
4.conect195
5.incomet
6.enorvesion
7.https://scico7.com/
8.
"""

def editbatch(request, id):
    batch=Batch.objects.get(id=id)
    if request.method=="POST":
        batch.name=request.POST['batch']
        batch.save()
        return redirect('batch')
    return render(request,'managment/editbatch.html', {'batch':batch.name} )    

def fronbatcdeleteuser(request, id):
   groupgser =GroupUser.objects.get(id=id)
   groupgser.is_active=0
   groupgser.delete()
   return redirect('batch')


def relative(request):
    if request.method:
        pass

    return render(request,'managment/relative.html')

def createsession(request):
    if request.method=='POST':
        name=request.POST['createevent']
        time=request.POST['time1']
        date=request.POST['date']
        event=Event()
        event.name=name
        event.time= time
        event.date= date

        event.save()
        return redirect("batch")
    return render(request, 'managment/createsession.html')    



def editsession(request, id):
    event=Event.objects.get(id=id)

    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['date'] 
        time=request.POST['time']
        event.name=name
        event.date=date
        event.time=time
        
        event.save()
        return redirect('session')

    return render(request,'managment/editsession.html', {'event':event})    
    
def sessionactive(request,id):
    event=Event.objects.get(id=id)
    event.is_active=True
    event.save()
    return redirect("session")


def sessiondeactive(request,id):
    event=Event.objects.get(id=id)
    event.is_active=False 
    event.save()
    return redirect('session')    

    

# def sessiondeactive(request,id):
#     event=Event.objects.get(id=id)
#     event.is_active=False
#     event.save()
#     return redirect('session')   

def createtraner(request):
    if request.session['email']:
        test = None
    else:
        return render(request, 'login.html')

    languages=Languages.objects.all()
    batch=Batch.objects.all()


    if request.method=="POST":
        trainer_name=request.POST['trainer_name']
        email=request.POST['email']
        batch =Batch.objects.get(name=request.POST['batch'])
        languages =Languages.objects.get(language=request.POST['language'])
        
        trainer=Trainer()
        trainer.trainer_name=trainer_name
        trainer.email=email
        trainer.batch=batch
        trainer.trand_by=languages
        trainer.save()
        return redirect('trainer')  
    return render(request, 'managment/createtrainer.html',{"languages":languages,"batch":batch})


def languages(request):
    if request.method=="POST":
        language=request.POST['language1']
        lag=Languages()
        lag.language=language
        lag.save()       
    return render(request,'managment/createlanguages.html')    


def traneractive(request,id):
    event=Trainer.objects.get(id=id)
    event.is_active=True
    event.save()
    return redirect('trainer')    
    

def trainerdeactive(request,id):
    event=Trainer.objects.get(id=id)
    event.is_active=False
    event.save()
    return redirect('trainer')   


    
        


    