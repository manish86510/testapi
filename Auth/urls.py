from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'city', views.CityViewSet, base_name='city')
router.register(r'education', views.MyEducationViewSet, base_name='education')
router.register(r'follower', views.MyFollowerViewSet, base_name='follower')
router.register(r'my-interest', views.MyInterestViewSet, base_name='interest')
router.register(r'language', views.MyLanguageViewSet, base_name='language')
router.register(r'places', views.MyPlaceViewSet, base_name='places')
router.register(r'projects', views.MyProjectViewSet, base_name='projects')
router.register(r'skill', views.MySkillViewSet, base_name='skill')
router.register(r'social-link', views.SocialLinkViewSet, base_name='social_link')
router.register(r'workplace', views.WorkplaceViewSet, base_name='workplace')
router.register(r'recommended', views.RecommendedViewSet, base_name='get_recomended_users')
router.register(r'language', views.LanguageViewSet, base_name='global_language')
router.register(r'skill', views.SkillViewSet, base_name='global_skill')
router.register(r'interest', views.InterestViewSet, base_name='global_interest')
router.register(r'me', views.UserViewSet, base_name='user')
router.register(r'register', views.UserViewSet, base_name='register')


urlpatterns = [
    path('', include(router.urls)),
    path('verify_mail/<str:code>', views.verifyMail, name='verify_mail'),
    path('profile-update', views.UserUpdateViewSet.as_view(), name='update_update'),
]
