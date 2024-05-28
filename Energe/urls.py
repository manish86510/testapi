from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Auth.views import *
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path,re_path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.conf.urls import url
from django.urls import path
from django.urls import path, re_path
# from posts import urls as posts_urls
from companyprofile.views import *
from rest_framework.routers import DefaultRouter




schema_view = get_schema_view(
   openapi.Info(
      title="Incomet API",
      default_version='v1',
      description="Demo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="info@enorvision.com"),
      license=openapi.License(name="Enorvision License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('gettoken/',TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(), name= 'token_refresh'),
    # path('verifytoken/',TokenVerifyView.as_view(), name='token_verify'),
    path('update_service/<int:pk>/', update_service),
    path('update_company/<int:pk>/', update_company),
    re_path(r'^company/add/', add_company, name='add_company'), 
    path('api/company/', get_all_company, name='get_all_company'),    
    re_path(r'^services/add/', add_service, name='add_service'), 
    path('api/services/', get_all_services, name='get_all_services'),
    path('api/industry/', get_all_industry, name='get_all_industry'),
    re_path(r'^industry/add/', add_industry, name='add_industry'), 
    path('update_industry/<int:pk>/', update_industry),
    path('api/delete_industry/<int:pk>/', delete_industry, name='delete_industry'),
    path('api/events/', get_all_events, name='get_all_events'),
    re_path(r'^events/add/', add_events, name='add_events'),
    path('api/news/', get_all_news, name='get_all_news'),
    re_path(r'^news/add/', add_news, name='add_news'),
    path('api/scheme/', get_all_scheme, name='get_all_scheme'),
    re_path(r'^scheme/add/', add_scheme, name='add_scheme'),
    path('api/leads/', get_all_leads, name='get_all_leads'),
    re_path(r'^leads/add/', add_leads, name='add_leads'),
    
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^user/', include('Auth.urls')),
    re_path(r'^api/v1/post/', include('Posts.urls')),
    re_path(r'^api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('', include('IncometAPI.urls')),
    re_path(r'^', include('IncometAPI.urls')),
    # re_path(r'^', include('companyprofile.urls')),
    # path('api/login', csrf_exempt(login), name='api_login'),
    # path('api/accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    # path('post/', include('Posts.urls')),
]
admin.site.site_header = 'Admin Dashboard'
# admin.site.site_title = 'Admin'
admin.site.site_url = 'http://incomet.com/'
admin.site.index_title = 'Administration'
admin.empty_value_display = '**Empty**'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
