from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from  Auth.models  import User
# from django.utils import timezone

class Employee():
    name = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)
    email = models.EmailField(unique=True) 
    token = models.CharField(max_length=255, blank=True, null=True)
    
class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] 
    

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='companies')
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=15)
    reg_number = models.CharField(max_length=20, validators=[MinLengthValidator(20), MaxLengthValidator(20)])
    reg_date = models.DateField()
    sector = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_companies')
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, default=1)
    is_verify = models.BooleanField(default=False)



class Service(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,unique=True)
    short_description = models.TextField()
    long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Events(models.Model):
    date=models.DateField()
    banner = models.ImageField(upload_to='events_banners/', default='path/to/default/image.jpg')
    short_desc=models.CharField(max_length=250)
    long_desc=models.TextField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    title=models.CharField(max_length=200,unique=True)
    guests=models.CharField(max_length=250)
    valid=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updted_at = models.DateTimeField(auto_now=True)
    
    
class News(models.Model):
    date=models.DateField()
    author=models.CharField(max_length=250)
    source=models.CharField(max_length=250)
    title=models.CharField(max_length=250, unique=True)
    short_desc=models.CharField(max_length=250)
    long_desc=models.TextField()
    banner = models.ImageField(upload_to='news_banners/', default='path/to/default/image.jpg')
    valid=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updted_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    
class Scheme(models.Model):
    name=models.CharField(max_length=250, unique=True)
    url = models.CharField(max_length=300)
    short_desc=models.CharField(max_length=250)
    long_desc=models.TextField()
    banner=models.ImageField(upload_to='scheme_banners/', default='path/to/default/image.jpg')
    launched_date=models.DateField()
    valid= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Leads(models.Model):
    company_id=models.ForeignKey('Company', on_delete=models.CASCADE)
    title=models.CharField(max_length=250, unique=True)
    description=models.TextField()
    attachment = models.FileField(upload_to='files_uploads/', default='files_uploads/default.pdf')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status=models.BooleanField(default=True)
    valid=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updted_at = models.DateTimeField(auto_now=True)
    
    
class Plan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    reference = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    
    
    

    
