from django.contrib import admin
from .models import *

# Register your models here.


class PostOptionsAdmin(admin.ModelAdmin):
    list_display = ('about_post', 'tags', 'like_count', 'share_count', 'comment_count', 'points_earner', 'created_by', 'created_at' ,'user', 'is_public', 'target_audience_interests', 'post_type')
    search_fields = ('about_post', 'tags', 'like_count', 'share_count', 'comment_count', 'points_earner', 'created_by', 'created_at' ,'user', 'is_public', 'target_audience_interests', 'post_type')


class PostMediaOptionsAdmin(admin.ModelAdmin):
    list_display = ('post', 'file', 'file_type')
    search_fields = ('post', 'file', 'file_type')


class PostLikesOptionsAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'activity')
    search_fields = ('post', 'user', 'activity')


class PostCommentsOptionsAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'comment', 'parent')
    search_fields = ('post', 'user', 'comment', 'parent')


class PostShareOptionsAdmin(admin.ModelAdmin):
    list_display = ('post', 'shared_by', 'description')
    search_fields = ('post', 'shared_by', 'description')


admin.site.register(Post, PostOptionsAdmin)
admin.site.register(PostMedia, PostMediaOptionsAdmin)
admin.site.register(PostLikes, PostLikesOptionsAdmin)
admin.site.register(PostComments, PostCommentsOptionsAdmin)
admin.site.register(PostShare, PostShareOptionsAdmin)