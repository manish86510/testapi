from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import follow
from django.urls import path,re_path
from django.urls import path, include
# from posts import urls as posts_urls

router = DefaultRouter()
# router.register(r'friends-list', views.FriendListViewSet, base_name='friends_list')
router.register(r'city', views.CityViewSet, basename='city')
router.register(r'education', views.MyEducationViewSet, basename='education')
router.register(r'follow', follow.FollowViewSet, basename='follow')
router.register(r'follower', follow.FollowerViewSet, basename='follower')
router.register(r'following', follow.FollowingViewSet, basename='following')
router.register(r'my-interest', views.MyInterestViewSet, basename='interest')
router.register(r'my-language', views.MyLanguageViewSet, basename='language')
router.register(r'places', views.MyPlaceViewSet, basename='places')
router.register(r'projects', views.MyProjectViewSet, basename='projects')
router.register(r'my-skill', views.MySkillViewSet, basename='skill')
router.register(r'social-link', views.SocialLinkViewSet, basename='social_link')
router.register(r'workplace', views.WorkplaceViewSet, basename='workplace')
router.register(r'recommended', views.RecommendedViewSet, basename='get_recomended_users')
router.register(r'language', views.LanguageViewSet, basename='global_language')
router.register(r'skill', views.SkillViewSet, basename='global_skill')
router.register(r'interest', views.InterestViewSet, basename='global_interest')
router.register(r'me', views.UserViewSet, basename='user')
router.register(r'register', views.UserViewSet, basename='register'),


urlpatterns = [
    re_path('', include(router.urls)),
    path('posts/', include('Posts.urls')),
    re_path(r'^profile-update/', views.UserUpdateViewSet.as_view(), name='update_update'),
    re_path(r'^generate_agora_token/ ', views.generate_token, name="generate_agora_token")
]
