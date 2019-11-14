from django.urls import path
from .views import *

urlpatterns = [
    path('create_post', CreatePostView.as_view(), name='createpostview'),
    path('post_media', PostMediaView.as_view(), name='postmediaview'),
    path('post_likes', PostLikesView.as_view(), name='postlikesview'),
    path('post_comments', PostCommentsView.as_view(), name='postcommentsview'),
    path('post_share', PostShareView.as_view(), name='postshareview'),
    path('get_all/posts', GetAllPostsView.as_view(), name='getallpostsview'),
    path('get_all/media', GetAllMediaView.as_view(), name='getallmediaview'),
    path('get_all/comments', GetAllCommentsView.as_view(), name='getallcommentsview'),
    path('get_all/shares', GetAllSharesView.as_view(), name='getallsharesview'),
    path('get_all/likes', GetAllLikesView.as_view(), name='getalllikesview'),
]
