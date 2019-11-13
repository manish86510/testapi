from django.urls import path
from .views import *

urlpatterns = [
    path('create_post', CreatePostView.as_view(), name='createpostview'),
    path('post_media', PostMediaView.as_view(), name='postmediaview'),
    path('post_likes', PostLikesView.as_view(), name='postlikesview'),
    path('post_comments', PostCommentsView.as_view(), name='postcommentsview'),
    path('post_share', PostShareView.as_view(), name='postshareview'),
]
