from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.PostViewSet, base_name='post')
# router.register(r'post/comment', views.PostCommentViewSet, base_name='comment')
router.register(r'media', views.PostMediaViewSet, base_name='media')

urlpatterns = [
    path('', include(router.urls)),
    path('media/<int:post_id>/', views.PostMediaViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    ), name='post_comment_list'),
    path('comment/<int:post_id>/', views.PostCommentViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    ), name='post_comment_list'),
    path('likes/<int:post_id>/', views.PostLikeViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    ), name='post_likes_list'),
    path('share/<int:post_id>/', views.PostShareViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
            'put': 'update',
            'delete': 'destroy'
        }
    ), name='post_share_list')
]
