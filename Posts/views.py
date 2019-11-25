from rest_framework import viewsets, permissions
from .models import *
# from .serializers import *
from .serializers.post import PostSerializer, PostCreateSerializer
from .serializers.post_media import PostMediaSerializer
from .swagger.post import PostSwaggerDoc
from .swagger.post_media import PostMediaSwagger
from django.utils.decorators import method_decorator


@method_decorator(name='create', decorator=PostSwaggerDoc.create())
@method_decorator(name='list', decorator=PostSwaggerDoc.list())
@method_decorator(name='destroy', decorator=PostSwaggerDoc.delete())
@method_decorator(name='update', decorator=PostSwaggerDoc.update())
@method_decorator(name='retrieve', decorator=PostSwaggerDoc.retrieve())
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [permissions.AllowAny, ]
    serializer_action_classes = {
        'list': PostSerializer,
        'create': PostCreateSerializer,
        'update': PostCreateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


@method_decorator(name='create', decorator=PostMediaSwagger.create())
@method_decorator(name='list', decorator=PostMediaSwagger.list())
@method_decorator(name='destroy', decorator=PostMediaSwagger.delete())
@method_decorator(name='update', decorator=PostMediaSwagger.update())
@method_decorator(name='retrieve', decorator=PostMediaSwagger.retrieve())
class PostMediaViewSet(viewsets.ModelViewSet):
    serializer_class = PostMediaSerializer
    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostMedia.objects.all()
        if self.kwargs.get('post_id'):
            queryset = queryset.filter(post=self.kwargs.get('post_id'))
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PostMediaViewSet, self).list(request, *args, **kwargs)

