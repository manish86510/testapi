from django.db import models
from django.contrib.auth import get_user_model
from Core.models import SoftDeleteModel

User = get_user_model()


class Post(SoftDeleteModel):
    POST_TYPES = (
        ('Post', 'Post'),
        ('Polls', 'Polls'),
        ('Project', 'Project'),
    )
    about_post = models.TextField(null=False, help_text='Write something about the post.')
    tags = models.CharField(max_length=200, null=True)
    like_count = models.IntegerField(default=0, help_text='Count of likes on this post.')
    share_count = models.IntegerField(default=0, help_text='Count of share on this post.')
    comment_count = models.IntegerField(default=0, help_text='Count of views on this post.')
    points_earner = models.IntegerField(default=0, help_text='Coin earn by this post.')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_public = models.BooleanField(default=True, help_text='Post not available for other users.')
    target_audience = models.CharField(max_length=200, null=True, help_text='Target audience should be profession '
                                                                            'of person. ie. Doctor, Teacher, '
                                                                            'Software Engineer etc.')
    post_type = models.CharField(max_length=50, default='Post', choices=POST_TYPES)

    def __str__(self):
        return self.about_post

    class Meta:
        verbose_name_plural = 'My Posts'
        db_table = 'posts'


class PostMedia(SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, related_name='post_media', null=True, default=None)
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
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Post Media'
        db_table = 'post_media'


class PostLikes(SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity = models.CharField(max_length=200, editable=False, default='Liked')
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = 'Post Likes'
        db_table = 'post_likes'


class PostComments(SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=False)
    parent = models.IntegerField(default=-1)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Post Comments'
        db_table = 'post_comments'


class PostShare(SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_share')
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'Post Share'
        db_table = 'post_share'


class PostTag(SoftDeleteModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tag')
    tagged_users = models.TextField(null=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'Post Tag'
        db_table = 'post_tag'
