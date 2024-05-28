from turtle import title
from django.db import models
from Auth.models import *
from django.core.validators import FileExtensionValidator
# from Posts.models import SomeModel
# Create your models here.

# class Video(models.Model):
#     name = models.FileField(upload_to='images/',null=True)

# class Docs(models.Model):
#     docs = models.FileField(upload_to='images/',null=True)    

# class TeacherProfile(models.Model):
#     name=models.CharField(max_length=200,null=True)
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     education_degree=models.CharField(max_length=200,null=True)
#     institute=models.CharField(max_length=200,null=True)
#     experience=models.CharField(max_length=200,null=True)
#     address=models.CharField(max_length=200,null=True)
#     no_of_classes=models.IntegerField()
#     address=models.CharField(max_length=200,null=True)
#     coverase=models.BooleanField()  
#     video = models.ForeignKey(Video,null=True, on_delete=models.CASCADE)
#     docs = models.ForeignKey(Video,null=True, on_delete=models.CASCADE)


class News(models.Model):
    subtitel=models.CharField(max_length=200,null=True)
    source_url=models.URLField( max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)   
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)

    def __str__(self):
        return self.subtitel

class FinanceNews(models.Model):
    title=models.CharField(max_length=200,null=True)
    subtitel=models.CharField(max_length=200,null=True)
    source_url=models.URLField( max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)   
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)

    def __str__(self):
        return self.subtitel

class IncometStories(models.Model):
    name=models.CharField(max_length=200,null=True)
    story=models.CharField(max_length=200,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)   
    image = models.ImageField(upload_to='stories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Descriptions(models.Model):
    title=models.CharField(max_length=200, null=True)
    file=models.ForeignKey(FinanceNews, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    discriptions=models.CharField(max_length=2000, null=True)
    def __str__(self):
        return self.title


class Courses(models.Model):
    courses_name=models.CharField(max_length=200, null=True)
    courses_discriptions=models.CharField(max_length=800, null=True)
    courses_start_date=models.DateField(max_length=200, null=True)
    courses_end_date=models.DateField(max_length=200, null=True)
    courses_pdf=models.FileField(upload_to='images/', null=True, blank=True)
    courses_price=models.IntegerField(null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)
    rating_number=models.IntegerField(null=True)
    number_of_user=models.IntegerField(null=True)
    def __str__(self):
        return self.courses_name

class Rating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE,)
    courses_rating=models.IntegerField(null=True)
    review=models.CharField(max_length=200,null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.review

class Cart(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_purchased = models.BooleanField(default=False)
    text=models.CharField(max_length=100, null=True,blank=True)
    def __str__(self):
        return self.text
    
    
    


class Begner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='begner/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.text


class Beginner(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='beginner/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.text


class Medium(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='medium/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.text




class Advance(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='advance/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.text


class Certificate(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200, null=True, blank=True)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='certificate/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)    
    def __str__(self):
        return self.text


    
class Learn(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    beginner=models.ForeignKey(Beginner,  related_name='beginner1',on_delete=models.CASCADE)
    medium=models.ForeignKey(Medium, related_name='medium1', on_delete=models.CASCADE)
    advance=models.ForeignKey(Advance, related_name='advance1', on_delete=models.CASCADE)
    certificate=models.ForeignKey(Certificate, related_name='certificate1', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='learn/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    Description=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name



class Lerner(models.Model):
    student_type = [
        ("beginner", 'beginner'),
        ("medium", 'medium'),
        ("advance", 'advance'),
        
    ]    

    type_of_lerner=models.CharField(max_length=200, choices=student_type)
    title=models.CharField(max_length=100,null=True,blank=True)
    discriptions=models.TextField()
    imange=models.ImageField(upload_to='certificate/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title






# class Batch(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

# class GroupUserBatch(models.Model):
#     group = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True, null=True)
#     is_active = models.BooleanField(default=True)
#     def __str__(self):
#         return self.group
        


    

# class Couse_Section(models.Model):
#     course=models.ForeignKey(Courses,null=True,blank=True, on_delete=models.CASCADE)    
#     user=models.ForeignKey(User,null=True, on_delete=models.CASCADE)
#     section_name=models.CharField(max_length=100,null=True,blank=True)
#     Description=models.TextField()
#     created_date= models.DateTimeField(auto_now_add=True, null=True)
#     update_date= models.DateTimeField(auto_now=True, null=True)
#     def __str__(self):
#         return self.section_name


# class Course_Review(models.Model):
#     user=models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
#     url=models.URLField(max_length = 200, null=True, blank=True)
#     video = models.FileField(upload_to='videos_uploaded/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])  
#     created_date= models.DateTimeField(auto_now_add=True, null=True)
#     update_date= models.DateTimeField(auto_now=True, null=True)




class Beginner1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    Descriptions=models.TextField()
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='beginner/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.title



    
class Medium1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    Descriptions=models.TextField()
    imange=models.ImageField(upload_to='medium/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.title



class Advance1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    Descriptions=models.TextField()
    imange=models.ImageField(upload_to='advance/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.title


class Certificate1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    text=models.TextField(null=True)
    imange=models.ImageField(upload_to='certificate/', null=True, blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True) 

    def __str__(self):
        return self.title

       






class Rating1(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    courses_rating=models.IntegerField(null=True)
    review=models.CharField(max_length=200,null=True,blank=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.review
class Couse_Section(models.Model):
    course=models.ForeignKey(Courses,null=True,blank=True, on_delete=models.CASCADE)    
    user=models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    section_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField()
    video = models.FileField(upload_to='videos_uploaded/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])  
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.section_name


class Course_Review(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    url=models.URLField(max_length = 200, null=True, blank=True)
    video = models.FileField(upload_to='videos_uploaded/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])  
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name

class Educator_Testimonial(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    imange=models.ImageField(upload_to='testimonial/', null=True, blank=True)
    discriptin=models.TextField()
    active=models.BooleanField(default=False)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True) 

    def __str__(self):
        return self.name


class Educator_Intorvideo(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    video = models.FileField(upload_to='educator_intorvideo/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])  
    active=models.BooleanField(default=False)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

class Educator(models.Model):
    educator_testimonial=models.ForeignKey(Educator_Testimonial,on_delete=models.CASCADE,null=True, blank=True)
    educator_intorvideo=models.ForeignKey(Educator_Intorvideo,on_delete=models.CASCADE,null=True, blank=True)
    active=models.BooleanField(default=False)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
            



class Category(models.Model):
    category=models.CharField(max_length=200,null=True,blank=True)
    title =models.CharField(max_length=200,null=True,blank=True)
    active=models.BooleanField(default=False)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return self.title
