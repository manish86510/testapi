from urllib import request
# from Posts.models import Post
from django.shortcuts import render
from rest_framework import viewsets, permissions,generics
from rest_framework.permissions import BasePermission
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
# from rest_framework.mixins import 
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

class Newsdetail(ModelViewSet):
    queryset = Descriptions.objects.all()
    serializer_class = DescriptionsSerializer
    permission_classes = (IsAuthenticated,)    
    
class News1(ModelViewSet):
    queryset = FinanceNews.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)   

class Stories(ModelViewSet):
    queryset = IncometStories.objects.all()
    serializer_class = IncometStoriesSerializer
    permission_classes = (IsAuthenticated,)  

class CoursesList(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAuthenticated,)  

# class CoursesList(generics.ListAPIView):
#     serializer_class = CoursesSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         rating = self.request.rating
#         return Rating.objects.filter(rating=rating)

# class CoursesList(ModelViewSet):
    
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
    
#     permission_classes = (IsAuthenticated,)      
    

class RatingList(ModelViewSet):
    queryset=Rating1.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)


class CartList(ModelViewSet):
    queryset=Cart.objects.filter(is_active=True).all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    

class BeginnerList(ModelViewSet):
    queryset = Beginner.objects.all()
    serializer_class = BeginnerSerializer
    permission_classes = (IsAuthenticated,)

class MediumList(ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer
    permission_classes = (IsAuthenticated,)


class AdvanceList(ModelViewSet):
    queryset = Advance.objects.all()
    serializer_class = AdvanceSerializer
    permission_classes = (IsAuthenticated,)    


class CertificateList(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = (IsAuthenticated,)    


class LearnList(ModelViewSet):
    queryset = Learn.objects.all()
    serializer_class = LearnSerializer
    permission_classes = (IsAuthenticated,)


class LernerBeginnerList(ModelViewSet):
    queryset = Lerner.objects.all().filter(type_of_lerner='beginner')
    serializer_class = LearnSerializerBeginner
    permission_classes = (IsAuthenticated,)

class LernerMediumList(ModelViewSet):
    queryset = Lerner.objects.all().filter(type_of_lerner='medium')
    serializer_class = LearnSerializerMedium
    permission_classes = (IsAuthenticated,)

class LernerAdvanceList(ModelViewSet):
    queryset = Lerner.objects.all().filter(type_of_lerner='advance')
    serializer_class = LearnSerializerAdvance
    permission_classes = (IsAuthenticated,)        

class CreateBatch(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = CreateBatchSerializer
    permission_classes = (IsAuthenticated,)

# class GroupCreateBatch(viewsets.ModelViewSet):
#     queryset = GroupUserBatch.objects.all()
#     serializer_class = CreateGroupUserBatchSerializer
#     permission_classes = (IsAuthenticated,)    


# class UserData(viewsets.ModelViewSet):
#     queryset = GroupUserBatch.objects.all()
#     serializer_class = UserDataSerializer
#     permission_classes = (IsAuthenticated,) 


class BuyCourse(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CourseBuySerializer
    permission_classes = (IsAuthenticated,)


class GetBuyCourse(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = GetCourseBuySerializer
    permission_classes = (IsAuthenticated,)



class My_Cource(viewsets.ModelViewSet):
    serializer_class = GetalldataSrializer
    permission_classes = (IsAuthenticated,) 

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user.id)
        return queryset

class CreateCouse_Section(viewsets.ModelViewSet):
    serializer_class = CreateCourse_SectionSerializer
    permission_classes = (IsAuthenticated,) 
    queryset=Couse_Section.objects.all()
    

class CreateViewCourse_Review(viewsets.ModelViewSet):
    serializer_class = CreateCourse_ReviewSerializer
    permission_classes = (IsAuthenticated,) 
    queryset=Course_Review.objects.all()
    

class GetCouse_Section(viewsets.ModelViewSet):
    serializer_class = Course_SectionSerializer
    permission_classes = (IsAuthenticated,) 
   

    def get_queryset(self):
        queryset = Couse_Section.objects.filter(user=self.request.user.id)
        return queryset

class GetCourse_Review(viewsets.ModelViewSet):
    serializer_class = Course_ReviewSerializer
    permission_classes = (IsAuthenticated,) 
    def get_queryset(self):
        queryset = Course_Review.objects.filter(user=self.request.user.id)
        return queryset        
    
class GetBegnnerData(viewsets.ModelViewSet):
    serializer_class = GetBeginnerDataSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Beginner1.objects.all()

class GetMediumData(viewsets.ModelViewSet):
    serializer_class = GetMediumDataSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Medium1.objects.all()


class GetAdvanceData(viewsets.ModelViewSet):
    serializer_class = GetAdvanceDataSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Advance1.objects.all()


class GetCertificateData(viewsets.ModelViewSet):
    serializer_class = GetCertificateDataSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Certificate.objects.all()


class Educator_TestimonialaView(viewsets.ModelViewSet):
    serializer_class = Educator_TestimonialSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Educator_Testimonial.objects.all()

class Educator_IntorvideoView(viewsets.ModelViewSet):
    serializer_class = Educator_IntorvideoSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Educator_Intorvideo.objects.all()

class EducatorsView(viewsets.ModelViewSet):
    serializer_class = EducatorSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Educator.objects.all()    


class CreateEducators(viewsets.ModelViewSet):
    serializer_class = CreateEducatorSrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Educator.objects.all()   




class CategoryAPI(viewsets.ModelViewSet):
    serializer_class = CategorySrializers
    permission_classes = (IsAuthenticated,) 
    queryset=Category.objects.all()        