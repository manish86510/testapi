from django.urls import path
from rest_framework import routers
from .views import CreatePostView


# router = routers.DefaultRouter()
# router.register(r'posts', CreatePostView, basename='PostViewSet')
#
# urlpatterns = router.urls
#
urlpatterns = [
    path('', CreatePostView.as_view(), name='createpostview'),
]