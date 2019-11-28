from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register(r'post/comment', views.PostCommentViewSet, base_name='comment')
router.register(r'media', views.PostMediaViewSet, base_name='media')
router.register(r'comment', views.PostCommentViewSet, base_name='comment')
router.register(r'like', views.PostLikeViewSet, base_name='like')
router.register(r'share', views.PostShareViewSet, base_name='share')
router.register(r'', views.PostViewSet, base_name='post')

urlpatterns = [
    path('', include(router.urls)),
    # path('media/', views.PostMediaViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='post_comment_list'),
    # path('comment/', views.PostCommentViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='post_comment_list'),
    # path('likes/', views.PostLikeViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='post_likes_list'),
    # path('share/', views.PostShareViewSet.as_view(
    #     {
    #         'get': 'list',
    #         # 'get': 'retreive',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='post_share_list')
]
