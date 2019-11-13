from django.db import models
from Auth.models import User


# Create your models here.
class Post(models.Model):
    about_post = models.TextField(null=False)
    tags = models.CharField(max_length=200, null=True)
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    points_earner = models.IntegerField(default=0)
    created_by = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    target_audience_interests = models.CharField(max_length=200, null=True)
    post_type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.about_post

    class Meta:
        verbose_name_plural = 'My Posts'
        db_table = 'posts'


class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='images/', null=True)
    file_types = (
        ("Image", "image"),
        ("PDF", "pdf"),
        ("doc", "doc"),
        ("docx", "docx"),
        ("xls", "xls"),
        ("xlsx", "xlsx"),
    )
    file_type = models.CharField(max_length=5, choices=file_types, default="Image")

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'Post Media'
        db_table = 'post_media'


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200, editable=False, default='Liked')

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = 'Post Likes'
        db_table = 'post_likes'


class PostComments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False)
    parent = models.IntegerField(default=1)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Post Comments'
        db_table = 'post_comments'


class PostShare(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'Post Share'
        db_table = 'post_share'
