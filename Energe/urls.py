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
    path('admin/', admin.site.urls),
    path('verify-company/', verify_company, name='verify_company'),
    # path('api/', include('companyprofile.urls')), 
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('api/token/',TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name= 'token_refresh'),
    # path('verifytoken/',TokenVerifyView.as_view(), name='token_verifsy'),
    path('service/', service_view, name='service_view'),  # For GET all and POST new
    path('service/<int:pk>/', service_view, name='service_detail'),  # For GET by ID and PUT
    path('company/', company_view, name='company_view'),  # For GET all and POST new
    path('company/<int:id>/', company_view, name='company_detail'),  # For GET by ID    
    
    path('industry/', industry_view, name='industry_view'),  # For GET all and POST new
    path('industry/<int:pk>/', industry_view, name='industry_detail'),  # For GET, PUT, DELETE by ID
    path('events/', events_view, name='events_view'), 
    path('events/<int:pk>/', events_view, name='events_detail'), 
    path('news/', news_view, name='news_view'),
    path('news/<int:pk>/', news_view, name='news_detail'), 
    
    path('schemes/', scheme_view, name='scheme_view'),  # For GET all and POST new
    path('schemes/<int:pk>/', scheme_view, name='scheme_detail'),
    
    path('leads/', leads_view, name='leads_view'),  # For GET all and POST new
    path('leads/<int:pk>/', leads_view, name='leads_detail'), 
    
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
