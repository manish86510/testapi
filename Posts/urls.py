from django.urls import path, include
from .views import *

urlpatterns = [
    path('create_post', CreatePostView.as_view(), name='createpostview'),
    path('post_media', PostMediaView.as_view(), name='postmediaview'),
    path('post_likes', PostLikesView.as_view(), name='postlikesview'),
    path('post_comments', PostCommentsView.as_view(), name='postcommentsview'),
    path('post_share', PostShareView.as_view(), name='postshareview'),
    path('get_all/', include([
        path('posts', GetAllPostsView.as_view(), name='getallpostsview'),
        path('media', GetAllMediaView.as_view(), name='getallmediaview'),
        path('comments', GetAllCommentsView.as_view(), name='getallcommentsview'),
        path('shares', GetAllSharesView.as_view(), name='getallsharesview'),
        path('likes', GetAllLikesView.as_view(), name='getalllikesview'),
    ])),
    path('get_by_id/', include([
        path('posts', GetPostsById.as_view(), name='get_post_by_id'),
        path('media', GetMediaById.as_view(), name='get_media_by_id'),
        path('comments', GetCommentsById.as_view(), name='get_comments_by_id'),
        path('shares', GetSharesById.as_view(), name='get_shares_by_id'),
        path('likes', GetLikesById.as_view(), name='get_likes_by_id'),
    ])),
]
