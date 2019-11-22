from rest_framework import viewsets, permissions
from .models import *
# from .serializers import *
from .serializers.post import PostSerializer, PostCreateSerializer
from .serializers.post_media import PostMediaSerializer
from .serializers.post_comments import PostCommentSerializer
from .serializers.post_likes import PostLikeSerializer
from .serializers.post_share import PostShareSerializer
from .swagger.post import PostSwaggerDoc
from .swagger.post_media import PostMediaSwagger
from .swagger.post_comments import PostCommentSwagger
from .swagger.post_likes import PostLikeSwagger
from .swagger.post_share import PostShareSwagger
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
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PostMediaViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=PostCommentSwagger.create())
@method_decorator(name='list', decorator=PostCommentSwagger.list())
@method_decorator(name='destroy', decorator=PostCommentSwagger.delete())
@method_decorator(name='update', decorator=PostCommentSwagger.update())
@method_decorator(name='retrieve', decorator=PostCommentSwagger.retrieve())
class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostComments.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PostCommentViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=PostLikeSwagger.create())
@method_decorator(name='list', decorator=PostLikeSwagger.list())
@method_decorator(name='destroy', decorator=PostLikeSwagger.delete())
@method_decorator(name='update', decorator=PostLikeSwagger.update())
@method_decorator(name='retrieve', decorator=PostLikeSwagger.retrieve())
class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer
    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostLikes.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PostLikeViewSet, self).list(request, *args, **kwargs)


@method_decorator(name='create', decorator=PostShareSwagger.create())
@method_decorator(name='list', decorator=PostShareSwagger.list())
@method_decorator(name='destroy', decorator=PostShareSwagger.delete())
@method_decorator(name='update', decorator=PostShareSwagger.update())
@method_decorator(name='retrieve', decorator=PostShareSwagger.retrieve())
class PostShareViewSet(viewsets.ModelViewSet):
    serializer_class = PostShareSerializer
    # http_method_names = ['post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostShare.objects.all()
        return queryset

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PostShareViewSet, self).list(request, *args, **kwargs)

