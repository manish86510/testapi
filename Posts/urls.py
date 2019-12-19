from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'notification', views.NotificationsViewSet, base_name='notification')
router.register(r'hot-topic', views.HotTopicViewSet, base_name='hot_topic')
router.register(r'media', views.PostMediaViewSet, base_name='media')
router.register(r'comment', views.PostCommentViewSet, base_name='comment')
router.register(r'like', views.PostLikeViewSet, base_name='like')
router.register(r'share', views.PostShareViewSet, base_name='share')
router.register(r'', views.PostViewSet, base_name='post')

urlpatterns = [
    # path('get-post/', views.GetPostsViewSet.as_view(), name='posts_list'),
    path('', include(router.urls)),
]
