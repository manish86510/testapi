from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    salutation = models.CharField(max_length=500, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    about = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    cover_picture = models.ImageField(upload_to='coverPicture/', null=True, blank=True)
    posts_count = models.IntegerField(null=True, blank=True)
    followers_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    skills = models.TextField(null=True)
    address = models.TextField(null=True)
    enlarge_url = models.URLField(null=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, null=True)
    birth_place = models.CharField(max_length=500, null=True)
    gender = models.CharField(max_length=20, null=True)
    is_mail_verified = models.BooleanField(default=False)
    verify_mail_code = models.TextField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'user'
        db_table = 'user'


class City(models.Model):
    city_name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=20)
    created_by = models.IntegerField(default=0)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'Cities'
        db_table = 'city'


class WorkPlace(models.Model):
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    working_from = models.DateTimeField(auto_now_add=False)
    working_till = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Work Places'
        db_table = 'work_place'


class Education(models.Model):
    school_college_name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    session_from = models.DateTimeField(auto_now_add=False)
    session_to = models.DateTimeField(auto_now_add=False)
    attended_for = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_college_name

    class Meta:
        verbose_name_plural = 'Education'
        db_table = 'education'


class MyPlaces(models.Model):
    place_name = models.CharField(max_length=200, null=True)
    lat_long = models.CharField(max_length=200, null=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name_plural = 'My Places'
        db_table = 'place'


class SocialLinks(models.Model):
    name = models.CharField(max_length=200, null=True)
    unique_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social Links'
        db_table = 'social_links'


class MyLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    read = models.CharField(max_length=200, null=True)
    write = models.CharField(max_length=200, null=True)
    speak = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        db_table = 'language'


class MyProjects(models.Model):
    project_title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    skills = models.TextField(null=True)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    team_size = models.IntegerField(null=True)
    client_name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name_plural = 'My Projects'
        db_table = 'projects'


class MyInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interact_code = models.IntegerField(null=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'My Interest'
        db_table = 'interest'
