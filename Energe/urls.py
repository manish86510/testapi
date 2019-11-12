from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Auth.views import *
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="Energe API",
      default_version='v1',
      description="Demo",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="energe@skysoft.local"),
      license=openapi.License(name="skysoft License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('Auth.urls')),
    path('api/', include([
        path('token/', include([
            path('', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        ])),
        path('login', csrf_exempt(login), name='api_login'),
        path('accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    ])),
    path('posts/', include('Posts.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'Admin'
admin.site.site_url = 'http://Energe.com/'
admin.site.index_title = 'Administration'
admin.empty_value_display = '**Empty**'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
