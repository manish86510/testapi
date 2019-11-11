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

from rest_framework_swagger.views import get_swagger_view

schema_view1 = get_swagger_view(title='Auth API')
schema_view2 = get_swagger_view(title='Post API')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-urls/', include('Auth.urls')),
    path('api/', include([
        path('token/', include([
            path('', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        ])),
        # path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        # path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        path('login', csrf_exempt(login), name='api_login'),
        path('accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    ])),
    # path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/login', csrf_exempt(login), name='api_login'),
    # path('api/accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    path('swaggertest/', schema_view1),
    path('posts/', include('Posts.urls')),
    path('api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'Admin'
admin.site.site_url = 'http://Energe.com/'
admin.site.index_title = 'Administration'
admin.empty_value_display = '**Empty**'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
