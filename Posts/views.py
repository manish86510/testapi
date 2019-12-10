from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, views
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .helpers import modify_input_for_multiple_files, return_list
from .models import *
# from .serializers import *
from .serializers.post import PostSerializer, PostCreateSerializer, PostAllDetailSerializer
from .serializers.post_media import PostMediaSerializer, PostMediaCreateSerializer
from .serializers.post_comments import *
from .serializers.post_likes import PostLikeSerializer
from .serializers.post_share import PostShareSerializer
from .serializers.post_tag import PostTagSerializer
from .serializers.get_full_post_info import GetFullPostInfoSerializer
from Auth.serializers.user import UserSerializer

from .swagger.post import PostSwaggerDoc, HotTopicSwaggerDoc
from .swagger.post_media import PostMediaSwagger
from .swagger.post_comments import PostCommentSwagger
from .swagger.post_likes import PostLikeSwagger
from .swagger.post_share import PostShareSwagger
from .swagger.post_tag import PostTagSwagger
from .swagger.get_full_post_info import GetFullPostSwagger

from django.utils.decorators import method_decorator
from django.http import JsonResponse
# from requests import Response
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.db.models import Q
from rest_framework.response import Response
from django.utils import timezone


# from rest_framework.permissions import IsAuthenticated
@method_decorator(name='list', decorator=HotTopicSwaggerDoc.list())
class HotTopicViewSet(viewsets.ModelViewSet):
    serializer_class = PostAllDetailSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-id')[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


@method_decorator(name='create', decorator=PostSwaggerDoc.create())
@method_decorator(name='list', decorator=PostSwaggerDoc.list())
@method_decorator(name='destroy', decorator=PostSwaggerDoc.delete())
@method_decorator(name='update', decorator=PostSwaggerDoc.update())
@method_decorator(name='retrieve', decorator=PostSwaggerDoc.retrieve())
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_action_classes = {
        'list': PostAllDetailSerializer,
        'get': PostAllDetailSerializer,
        'retrieve': PostAllDetailSerializer,
        'update': PostCreateSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        queryset = Post.objects.filter(Q(user=self.request.user.id) | Q(is_public=True)).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

        if self.request.data.get('media_id'):
            for obj in PostMedia.objects.filter(id__in=self.request.data.get('media_id')):
                obj.post = post
                obj.save()
        if self.request.data.get('media'):
            for media in self.request.data.get('media'):
                post_media = PostMedia(
                    media_url=media.get('url'),
                    media_type=media.get('mediaType'),
                    post=post
                )
                post_media.save()
        # serializer_obj = PostAllDetailSerializer(post)
        # return Response(serializer_obj.data, status=HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        query = Post.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=PostMediaSwagger.create())
@method_decorator(name='list', decorator=PostMediaSwagger.list())
@method_decorator(name='destroy', decorator=PostMediaSwagger.delete())
@method_decorator(name='update', decorator=PostMediaSwagger.update())
@method_decorator(name='retrieve', decorator=PostMediaSwagger.retrieve())
class PostMediaViewSet(viewsets.ModelViewSet):
    serializer_class = PostMediaCreateSerializer
    parser_classes = (MultiPartParser, FormParser)

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostMedia.objects.all()
        if self.kwargs.get('post'):
            queryset = queryset.filter(post=self.kwargs.get('post'))
        return queryset

    def create(self, request, *args, **kwargs):
        # post = Post.objects.get(id=int(request.data['post']))
        # converts querydict to original dict
        images = dict((request.data).lists())['file']
        type = request.data['file_type']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(request.data.get('post'),
                                                            img_name, type)
            file_serializer = PostMediaCreateSerializer(data=modified_data)
            if file_serializer.is_valid(raise_exception=True):
                file_serializer.save()
                arr.append(file_serializer.data.get('id'))
            else:
                flag = 0

        if flag == 1:
            return JsonResponse({"result": "Media Uploaded Successfully", "media_id": arr}, status=HTTP_200_OK,
                                safe=False)
        else:
            return JsonResponse(file_serializer.errors, status=HTTP_400_BAD_REQUEST, safe=False)

    def destroy(self, request, *args, **kwargs):
        query = PostMedia.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=PostCommentSwagger.create())
@method_decorator(name='list', decorator=PostCommentSwagger.list())
@method_decorator(name='destroy', decorator=PostCommentSwagger.delete())
@method_decorator(name='update', decorator=PostCommentSwagger.update())
@method_decorator(name='retrieve', decorator=PostCommentSwagger.retrieve())
class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        # queryset = PostComments.objects.all()
        queryset = PostComments.objects.filter(post=self.request.GET.get('post_id'))
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = PostCommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment_obj = serializer.save()
            comment_obj.user = self.request.user
            comment_obj.save()
            comment_obj.post.comment_count += 1
            comment_obj.post.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        query = PostComments.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.post.comment_count -= 1
        query.post.save()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


@method_decorator(name='create', decorator=PostLikeSwagger.create())
@method_decorator(name='list', decorator=PostLikeSwagger.list())
@method_decorator(name='destroy', decorator=PostLikeSwagger.delete())
@method_decorator(name='update', decorator=PostLikeSwagger.update())
@method_decorator(name='retrieve', decorator=PostLikeSwagger.retrieve())
class PostLikeViewSet(viewsets.ModelViewSet):
    serializer_class = PostLikeSerializer

    http_method_names = ['get', 'put', 'post', 'delete']

    def get_queryset(self):
        queryset = PostLikes.objects.filter(user=self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_class = PostLikeSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            post_like_query = PostLikes.objects.filter(post_id=request.data.get('post'), user=request.user).first()
            if not post_like_query:
                like_obj = serializer_class.save(post_id=request.data.get('post'), user=request.user)
                like_obj.post.like_count += 1
                like_obj.post.save()
                return JsonResponse("Like Saved Successfully", status=HTTP_200_OK, safe=False)
            else:
                post_like_query.post.like_count -= 1
                post_like_query.post.save()
                post_like_query.hard_delete()
                return JsonResponse("Unlike Saved Successfully", status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse(serializer_class.errors, status=HTTP_400_BAD_REQUEST, safe=False)

    def destroy(self, request, *args, **kwargs):
        ui = request.user.id
        un = User.objects.get(id=ui)
        user_name = un.username
        saved_likes = get_object_or_404(PostLikes.objects.all(), id=self.kwargs['pk'], user=ui)
        # post_name = saved_likes.post
        post_obj = Post.objects.get(id=saved_likes.post_id)
        # post_obj = Post.objects.get(about_post=post_name)
        post_obj.like_count -= 1
        post_obj.save()
        saved_likes.deleted_on = timezone.now()
        saved_likes.delete()
        return JsonResponse(
            {"message": "Like on post {} created by user {} has been deleted.".format(saved_likes.post_id, user_name)},
            status=204, safe=False)


@method_decorator(name='create', decorator=PostShareSwagger.create())
@method_decorator(name='list', decorator=PostShareSwagger.list())
@method_decorator(name='destroy', decorator=PostShareSwagger.delete())
@method_decorator(name='update', decorator=PostShareSwagger.update())
@method_decorator(name='retrieve', decorator=PostShareSwagger.retrieve())
class PostShareViewSet(viewsets.ModelViewSet):
    serializer_class = PostShareSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        queryset = PostShare.objects.filter(shared_by=self.request.user.pk)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer_class = PostShareSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            share_obj = serializer_class.save(post_id=request.data.get('post'), shared_by=request.user)
            share_obj.post.share_count += 1
            share_obj.post.save()
            return JsonResponse("Saved Successfully", status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse("Something is wrong", status=HTTP_400_BAD_REQUEST, safe=False)

    def destroy(self, request, *args, **kwargs):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), id=pk)
        post_name = saved_shares.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_shares.delete()
        return JsonResponse({"message": "Shared Post with id {} has been deleted.".format(pk)}, status=204, safe=False)


@method_decorator(name='create', decorator=PostTagSwagger.create())
@method_decorator(name='list', decorator=PostTagSwagger.list())
@method_decorator(name='destroy', decorator=PostTagSwagger.delete())
@method_decorator(name='update', decorator=PostTagSwagger.update())
@method_decorator(name='retrieve', decorator=PostTagSwagger.retrieve())
class PostTagViewSet(viewsets.ModelViewSet):
    serializer_class = PostTagSerializer

    http_method_names = ['get', 'put', 'post', 'delete']

    def get_queryset(self):
        queryset = PostTag.objects.filter(user=self.request.user.id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        query = PostTag.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=HTTP_200_OK)


#
# @method_decorator(name='list', decorator=GetFullPostSwagger.list())
# @method_decorator(name='retrieve', decorator=GetFullPostSwagger.retrieve())
# class GetPostsViewSet(viewsets.ModelViewSet):
#     # serializer_class = GetFullPostInfoSerializer
#
#     http_method_names = ['get']
#
#     def get_queryset(self):
#         import pdb
#         pdb.set_trace()
#         queryset = Post.objects.all()
#         # for post in posts:
#         #     media = PostMedia.objects.filter(post = post.pk)
#         #     comments = PostComments.objects.filter(post=post.pk)
#         #     likes = PostLikes.objects.filter(post=post.pk)
#         #     shares = PostShare.objects.filter(post=post.pk)
#         #     tags = PostTag.objects.filter(post=post.pk)
#         return queryset
#
#         # queryset = Post.objects.filter(user=self.request.user.id)
#         # return queryset
#     #
#     # def perform_create(self, serializer):
#     #     post = serializer.save()
#     #     post.user = self.request.user
#     #     post.save()

@method_decorator(name='get', decorator=GetFullPostSwagger.list())
# @method_decorator(name='get', decorator=GetFullPostSwagger.retrieve())
class GetPostsViewSet(views.APIView):
    serializer_class = PostAllDetailSerializer
    http_method_names = ['get']

    def get(self, request):
        posts = Post.objects.filter(user=request.user.id).order_by('-id')
        serializer = PostAllDetailSerializer(posts, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
