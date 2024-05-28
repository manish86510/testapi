# from dataclasses import field
from pyexpat import model
import json

from .models import *
from Auth.serializers.user import UserSerializer

from rest_framework import serializers
from Auth.models import *

# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'salutation', 'first_name', 'last_name', 'about', 'avatar',
#             'cover_picture', 'skills', 'address', 'enlarge_url', 'date_of_birth',
#             'birth_place', 'gender'
#         )

class DescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptions
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceNews
        fields = '__all__'  

class IncometStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncometStories
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    # rating=serializers.SerializersMethodField(read_only=True)
    rating_number = serializers.SerializerMethodField()
    number_of_user = serializers.SerializerMethodField()
    group_of_rating = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = ['id','courses_name','courses_discriptions','courses_start_date','courses_end_date','courses_pdf','courses_price','created_date','update_date','is_active','is_verify','number_of_user','rating_number','group_of_rating'] 


    # def get_rating_number(self, obj):
    #     # rating = Rating.objects.filter(courses_rating=5).values()
    #     rating = Rating.objects.filter(courses=obj)
    #     for i in rating:
    #         return i.courses_rating


    def get_rating_number(self, obj):
        rating = Rating1.objects.filter(course=obj).values()
        return rating  

    # def get_number_of_user(self, obj):
    #     user1=Rating1.objects.filter(user).count()
    #     print(user1)
    #     # for i in user1:
    #     return user1

    def get_number_of_user(self, obj):
        user1=Rating1.objects.filter(course=obj).count()
        print(user1)
        # for i in user1:
        return user1 


    def get_group_of_rating(self,obj):
        rdict={
            'rating5count':0,
            'rating4count':0,
            'rating3count':0,
            'rating2count':0,
            'rating1count':0,
        }   
        rting_group=Rating1.objects.filter(course=obj)
        r5=0
        r4=0
        r3=0
        r2=0
        r1=0
        for i in rting_group:
            if i.courses_rating==5:
                r5=r5+1
                rdict['rating5count']=r5
            elif i.courses_rating==4:
                r4=r4+1
                rdict['rating4count']=r4  
            elif i.courses_rating==3:
                r3=r3+1
                rdict['rating3count']=r3   
            elif i.courses_rating==2:
                r2=r2+1
                rdict['rating2count']=r2    

            elif i.courses_rating==1:
                r1=r1+1
                rdict['rating1count']=r1 
        dj=json.dumps(rdict)        

        return dj          
    

                          

    # def get_rating_number(self, obj):
    #     rating = Rating.objects.filter(courses_rating=5).values()
    #     return rating

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User 
#         fields = '__all__'   

class GetCourseBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' 
    
class RatingSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(read_only=True)
    class Meta:
        model = Rating1
        fields = '__all__' 

class CartSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"

class BeginnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beginner
        fields='__all__'  


class MediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medium 
        fields='__all__'  


class AdvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advance 
        fields='__all__'  


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate 
        fields='__all__'              


class LearnSerializer(serializers.ModelSerializer):
    beginner1 = BeginnerSerializer(read_only=True, many=True)
    # medium1 = MediumSerializer(read_only=True, many=True)
    # advance1 = AdvanceSerializer(read_only=True, many=True)
    # certificate1 = CertificateSerializer(read_only=True, many=True)
    class Meta:
        model = Learn 
        fields='__all__'             


class LearnSerializerBeginner(serializers.ModelSerializer):
    class Meta:
        model = Lerner 
        fields='__all__'


class LearnSerializerMedium(serializers.ModelSerializer):
    class Meta:
        model = Lerner 
        fields='__all__'


class LearnSerializerAdvance(serializers.ModelSerializer):
    class Meta:
        model = Lerner 
        fields='__all__'        



class CreateBatchSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault()
)
    class Meta:
        model = Batch 
        fields='__all__'     

    # def validate_user(self, value):         
    #     return self.context['request'].user     
    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["created_by"] = self.fields["created_by"].get_default()
        return super().save(**kwargs)





# class CreateGroupUserBatchSerializer(serializers.ModelSerializer): 
#     group=CreateBatchSerializer()
#     user=UserSerializer()
#     class Meta:
#         model = GroupUserBatch 
#         fields=['id','group',"user"]


# class UserDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupUserBatch 
#         fields=['id','group',"user"]


class CourseBuySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    class Meta:
        model=Cart
        fields='__all__'
    def save(self, **kwargs):
        kwargs["user"] = self.fields["user"].get_default()
        kwargs['is_purchased']=True
        return super().save(**kwargs) 
    # user=serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    # class Meta:
    #     model=Cart
    #     fields="__all__"

    # def save(self, **kwargs):
    #     kwargs["user"] = self.fields["user"].get_default()
    #     kwargs['is_purchased']=True
    #     return super().save(**kwargs)    


    # user=serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    # class Meta:
    #     model=Cart
    #     fields="__all__"

    # def save(self, **kwargs):
    #     kwargs["user"] = self.fields["user"].get_default()
    #     kwargs['is_purchased']=True
    #     return super().save(**kwargs)

        



class GetalldataSrializer(serializers.ModelSerializer):
    course = CoursesSerializer(read_only=True)
    user=UserSerializer(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'



class CreateCourse_SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Couse_Section
        fields="__all__"

class Course_SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Couse_Section
        fields="__all__"        

class Course_ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Course_Review
        fields="__all__"

class CreateCourse_ReviewSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True,default=serializers.CurrentUserDefault())
    class Meta:
        model=Course_Review
        fields="__all__"

    def save(self, **kwargs):
        kwargs["user"] = self.fields["user"].get_default()
        return super().save(**kwargs)     

class GetBeginnerDataSrializers(serializers.ModelSerializer):
    class Meta:
        model=Beginner1
        fields='__all__'

class GetMediumDataSrializers(serializers.ModelSerializer):
    class Meta:
        model=Medium1
        fields='__all__'

class GetAdvanceDataSrializers(serializers.ModelSerializer):
    class Meta:
        model=Advance1
        fields='__all__'

class GetCertificateDataSrializers(serializers.ModelSerializer):
    class Meta:
        model=Certificate1
        fields='__all__'


class Educator_TestimonialSrializers(serializers.ModelSerializer):
    class Meta:
        model=Educator_Testimonial
        fields="__all__"


class Educator_IntorvideoSrializers(serializers.ModelSerializer):
    class Meta:
        model=Educator_Intorvideo
        fields="__all__"
        
class EducatorSrializers(serializers.ModelSerializer):
    educator_testimonial=Educator_TestimonialSrializers(read_only=True)
    educator_intorvideo=Educator_IntorvideoSrializers(read_only=True)


    # testimonial= serializers.SerializerMethodField()
    class Meta:
        model=Educator
        fields=['educator_testimonial','educator_intorvideo',]

    # def get_testimonial(self, obj):
    #    testimonial1 = Educator_Testimonial.objects.filter(name=obj).values()
    #    return testimonial1     


class CreateEducatorSrializers(serializers.ModelSerializer):
    class Meta:
        model=Educator
        fields='__all__'




class CategorySrializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    