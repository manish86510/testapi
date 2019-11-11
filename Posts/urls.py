from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = []

#
# router = routers.DefaultRouter()
# router.register(r'posts', CreatePostView, base_name='PostViewSet')
# router.register(r'post_media', PostMediaView, base_name='postmediaview')
# router.register(r'post_likes', PostLikesView, base_name='postlikesview')
# router.register(r'post_comments', PostCommentsView, base_name='postcommentsview')
# router.register(r'post_share', PostShareView, base_name='postshareview')
#
# urlpatterns += router.urls

urlpatterns = [
    path('create_post', CreatePostView.as_view(), name='createpostview'),
    path('post_media', PostMediaView.as_view(), name='postmediaview'),
    path('post_likes', PostLikesView.as_view(), name='postlikesview'),
    path('post_comments', PostCommentsView.as_view(), name='postcommentsview'),
    path('post_share', PostShareView.as_view(), name='postshareview'),
]