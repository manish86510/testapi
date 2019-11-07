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
#from rest_framework_swagger.views import get_swagger_view

#schema_view1 = get_swagger_view(title='Auth API')

admin.site.site_header = 'Admin Dashboard'
admin.site.site_title = 'Admin'
admin.site.site_url = 'http://Energe.com/'
admin.site.index_title = 'Administration'
admin.empty_value_display = '**Empty**'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login',csrf_exempt(login) , name='api_login'),
    path('api/accounts/password_reset/', csrf_exempt(password_reset), name='api_password_reset'),
    #path('swagertest/', schema_view1)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
