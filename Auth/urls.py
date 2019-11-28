from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'language', views.LanguageViewSet, base_name='global_language')
router.register(r'skill', views.SkillViewSet, base_name='global_skill')
router.register(r'interest', views.InterestViewSet, base_name='global_interest')
router.register(r'', views.UserViewSet, base_name='user')
router.register(r'user/city', views.CityViewSet, base_name='city')
router.register(r'user/education', views.MyEducationViewSet, base_name='education')
router.register(r'user/follower', views.MyFollowerViewSet, base_name='follower')
router.register(r'user/interest', views.MyInterestViewSet, base_name='interest')
router.register(r'user/language', views.MyLanguageViewSet, base_name='language')
router.register(r'user/places', views.MyPlaceViewSet, base_name='places')
router.register(r'user/projects', views.MyProjectViewSet, base_name='projects')
router.register(r'user/skill', views.MySkillViewSet, base_name='skill')
router.register(r'user/social-link', views.SocialLinkViewSet, base_name='social_link')
router.register(r'user/workplace', views.WorkplaceViewSet, base_name='workplace')
# router.register(r'user/city', views.CityViewSet, base_name='city')


urlpatterns = [
    path('', include(router.urls)),
    path('verify_mail/<str:code>', views.verifyMail, name='verify_mail'),
    # path('city', views.CityViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='city_list'),
    # path('education', views.EducationViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='education_list'),
    # path('follower', views.FollowerViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='follower_list'),
    # path('interest', views.InterestViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='interest_list'),
    # path('language', views.LanguageViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='language_list'),
    # path('places', views.PlaceViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='places_list'),
    # path('project', views.ProjectViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='project_list'),
    # path('skill', views.SkillViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='skill_list'),
    # path('social-link', views.SocialLinkViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='social_link_list'),
    # path('workplace', views.WorkplaceViewSet.as_view(
    #     {
    #         'get': 'list',
    #         'post': 'create',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }
    # ), name='workplace_list'),


    # path('register', CreateUserView.as_view(), name='register'),
    # path('resend', ResendEmail.as_view(), name='resend_email'),
    # path('verify_mail/<str:code>', verifyMail, name='verify_mail'),
    # path('update_profile', UpdateProfile.as_view(), name='update_profile'),
    # path('education', MyEducation.as_view(), name='education'),
    # path('my_places', Places.as_view(), name='my_places'),
    # path('my_projects', Projects.as_view(), name='my_projects'),
    # path('work_place', MyWorkplace.as_view(), name='work_place'),
    # path('my_language', Language.as_view(), name='my_language'),
    # path('my_interest', Interest.as_view(), name='my_interest'),
    # path('my_social', Social.as_view(), name='my_social'),
    # path('get_by_id/', include([
    #     path('education', GetEducationById.as_view(), name='education_by_id'),
    #     path('places', GetPlacesById.as_view(), name='places_by_id'),
    #     path('projects', GetProjectsById.as_view(), name='projects_by_id'),
    #     path('workplace', GetWorkplaceById.as_view(), name='workplace_by_id'),
    #     path('language', GetLanguagesById.as_view(), name='languages_by_id'),
    #     path('interest', GetInterestsById.as_view(), name='interests_by_id'),
    #     path('social', GetSocialMediaById.as_view(), name='social_by_id'),
    # ])),
    # path('get_all/', include([
    #     path('user', GetUserAll.as_view(), name='user_all'),
    #     path('education', GetEducationAll.as_view(), name='education_all'),
    #     path('places', GetPlacesAll.as_view(), name='places_all'),
    #     path('projects', GetProjectsAll.as_view(), name='projects_all'),
    #     path('workplace', GetWorkplaceAll.as_view(), name='workplace_all'),
    #     path('language', GetLanguagesAll.as_view(), name='languages_all'),
    #     path('interest', GetInterestsAll.as_view(), name='interests_all'),
    #     path('social', GetSocialMediaAll.as_view(), name='social_all'),
    # ])),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

