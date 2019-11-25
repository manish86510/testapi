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
from requests import Response
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_200_OK



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

    def create(self, request, *args, **kwargs):
        pk = request.POST.get('post')
        ui = request.user.id
        serializer_class = PostLikeSerializer(data=request.data)
        if serializer_class.is_valid():
            try:
                post_det = PostLikes.objects.get(post=pk, user=ui)
            except PostLikes.DoesNotExist:
                post_det = None
            if post_det is None:
                serializer_class.save(post_id=pk)
                post_name = serializer_class.instance.post
                post_obj = Post.objects.get(about_post=post_name)
                post_obj.like_count += 1
                post_obj.save()
                return Response("Like Saved Successfully", status=HTTP_200_OK)
            else:
                return Response("Like already stored", status=HTTP_200_OK)
        else:
            return Response("Cannot Like the Post", status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        pk = request.POST.get('post')
        ui = request.user.id
        un = User.objects.get(id=ui)
        user_name = un.username
        saved_likes = get_object_or_404(PostLikes.objects.all(), post=pk, user=ui)
        post_name = saved_likes.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.like_count -= 1
        post_obj.save()
        saved_likes.delete()
        return Response({"message": "Like on post {} created by user {} has been deleted.".format(pk, user_name)},
                        status=204)

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

    def create(self, request, *args, **kwargs):
        pk = request.POST.get('post')
        ui = request.user
        serializer_class = PostShareSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk, shared_by=ui)
            post_name = serializer_class.instance.post
            post_obj = Post.objects.get(about_post=post_name)
            post_obj.share_count += 1
            post_obj.save()
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), id=pk)
        post_name = saved_shares.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_shares.delete()
        return Response({"message": "Shared Post with id {} has been deleted.".format(pk)}, status=204)

    # @action(methods=['get'], url_path='/<int:post_id>')
    def list(self, request, *args, **kwargs):
        return super(PostShareViewSet, self).list(request, *args, **kwargs)
