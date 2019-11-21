from django.contrib import admin
from Core.admin import BaseAdmin
from .models import *


class PostOptionsAdmin(BaseAdmin):
    list_display = ('about_post', 'tags', 'like_count', 'share_count', 'comment_count', 'points_earner',)
    search_fields = ('about_post', 'tags', 'like_count', 'share_count', 'comment_count', 'points_earner',)


class PostMediaOptionsAdmin(BaseAdmin):
    list_display = ('post', 'file', 'file_type')
    search_fields = ('post', 'file', 'file_type')


class PostLikesOptionsAdmin(BaseAdmin):
    list_display = ('post', 'user', 'activity')
    search_fields = ('post', 'user', 'activity')


class PostCommentsOptionsAdmin(BaseAdmin):
    list_display = ('post', 'user', 'comment', 'parent')
    search_fields = ('post', 'user', 'comment', 'parent')


class PostShareOptionsAdmin(BaseAdmin):
    list_display = ('post', 'shared_by', 'description')
    search_fields = ('post', 'shared_by', 'description')


admin.site.register(Post, PostOptionsAdmin)
admin.site.register(PostMedia, PostMediaOptionsAdmin)
admin.site.register(PostLikes, PostLikesOptionsAdmin)
admin.site.register(PostComments, PostCommentsOptionsAdmin)
admin.site.register(PostShare, PostShareOptionsAdmin)