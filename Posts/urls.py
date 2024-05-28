from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'batch', views.GroupViewSet, basename='batch')
router.register(r'tutor', views.TutorViewSet, basename='tutor')
router.register(r'batch_user', views.GroupUserViewSet, basename='batch_user')
router.register(r'group_message', views.ChatMessageViewSet, basename='group_message')
router.register(r'notification', views.NotificationsViewSet, basename='notification')
router.register(r'hot-topic', views.HotTopicViewSet, basename='hot_topic')
router.register(r'media', views.PostMediaViewSet, basename='media')
router.register(r'comment', views.PostCommentViewSet, basename='comment')
router.register(r'like', views.PostLikeViewSet, basename='like')
router.register(r'share', views.PostShareViewSet, basename='share')
router.register(r'', views.PostViewSet, basename='post')

urlpatterns = [
    # path('get-post/', views.GetPostsViewSet.as_view(), name='posts_list'),
    path('', include(router.urls)),
]
