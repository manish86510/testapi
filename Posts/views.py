from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, views
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .helpers import modify_input_for_multiple_files, return_list
from .models import *
# from .serializers import *
from .serializers.post import PostSerializer, PostCreateSerializer
from .serializers.post_media import PostMediaSerializer, PostMediaCreateSerializer
from .serializers.post_comments import PostCommentSerializer
from .serializers.post_likes import PostLikeSerializer
from .serializers.post_share import PostShareSerializer
from .serializers.post_tag import PostTagSerializer
from .serializers.get_full_post_info import GetFullPostInfoSerializer
from Auth.serializers.user import UserSerializer

from .swagger.post import PostSwaggerDoc
from .swagger.post_media import PostMediaSwagger
from .swagger.post_comments import PostCommentSwagger
from .swagger.post_likes import PostLikeSwagger
from .swagger.post_share import PostShareSwagger
from .swagger.post_tag import PostTagSwagger
from .swagger.get_full_post_info import GetFullPostSwagger

from django.utils.decorators import method_decorator
from django.http import JsonResponse
from requests import Response
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.db.models import Q
from django.utils import timezone


# from rest_framework.permissions import IsAuthenticated

@method_decorator(name='create', decorator=PostSwaggerDoc.create())
@method_decorator(name='list', decorator=PostSwaggerDoc.list())
@method_decorator(name='destroy', decorator=PostSwaggerDoc.delete())
@method_decorator(name='update', decorator=PostSwaggerDoc.update())
@method_decorator(name='retrieve', decorator=PostSwaggerDoc.retrieve())
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_action_classes = {
        'list': PostSerializer,
        # 'create': PostCreateSerializer,
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
        post = Post.objects.get(id=int(request.data['post']))

        # converts querydict to original dict
        images = dict((request.data).lists())['file']
        type = request.data['file_type']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(post,
                                                            img_name, type)
            file_serializer = PostMediaCreateSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return JsonResponse({"result": "Media Uploaded Successfully"}, status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse({"result": "Error Uploading Media"}, status=HTTP_400_BAD_REQUEST, safe=False)

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
        queryset = PostComments.objects.filter(user=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        post = serializer.save()
        post.user = self.request.user
        post.save()

    def destroy(self, request, *args, **kwargs):
        query = PostComments.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
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

    # def perform_create(self, serializer):
    #     try:
    #         post_det = PostLikes.objects.get(post=self.request.pk, user=self.request.user.id)
    #     except PostLikes.DoesNotExist:
    #         post_det = None
    #     if post_det is None:
    #         import pdb
    #         pdb.set_trace()
    #         serializer.save(post_id=self.request.pk)
    #         post_name = serializer.instance.post
    #         post_obj = Post.objects.get(about_post=post_name)
    #         post_obj.like_count += 1
    #         post_obj.save()
    #         return Response("Like Saved Successfully", status=HTTP_200_OK)
    #     else:
    #         return Response("Like already stored", status=HTTP_200_OK)

    # @api_view(['POST'])
    def create(self, request, *args, **kwargs):
        pk = request.data.get('post')
        ui = request.user.id
        # import pdb
        # pdb.set_trace()
        serializer_class = PostLikeSerializer(data=request.data)
        if serializer_class.is_valid():
            try:
                post_det = PostLikes.objects.get(post_id=pk, user_id=ui)
            except PostLikes.DoesNotExist:
                post_det = None
            if post_det is None:
                serializer_class.save(post_id=pk, user_id=ui)
                post_obj = Post.objects.get(id=pk)
                post_obj.like_count += 1
                post_obj.save()
                return JsonResponse("Like Saved Successfully", status=HTTP_200_OK, safe=False)
            else:
                return JsonResponse("Like already stored", status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse("Cannot Like the Post", status=HTTP_200_OK, safe=False)

    def destroy(self, request, *args, **kwargs):
        import pdb
        pdb.set_trace()
        # pk = request.POST.get('post')

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
        return JsonResponse({"message": "Like on post {} created by user {} has been deleted.".format(saved_likes.post_id, user_name)},
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
        pk = request.POST.get('post')
        ui = request.user
        serializer_class = PostShareSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk, shared_by=ui)
            post_name = serializer_class.instance.post
            post_obj = Post.objects.get(about_post=post_name)
            post_obj.share_count += 1
            post_obj.save()
            return JsonResponse("Saved Successfully", status=HTTP_200_OK, safe=False)
        else:
            return JsonResponse("Something is wrong", status=HTTP_200_OK, safe=False)

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
    serializer_class = GetFullPostInfoSerializer
    # model = Post
    # import pdb
    # pdb.set_trace()
    http_method_names = ['get']

    # @api_view(['GET'])
    # @swagger_auto_schema(
    #     tags=["Get Posts"],
    #     operation_summary="List Post",
    #     operation_description="List posts using the details provided by the user",
    #     responses={200: GetFullPostInfoSerializer(many=True)}
    # )
    def get(self, request):
        arr = []
        # import pdb
        # pdb.set_trace()
        posts = Post.objects.filter(user=request.user.id)
        for post in posts:
            post = post
            # import pdb
            # pdb.set_trace()
            media = return_list(PostMediaSerializer, PostMedia, post.pk)
            comments = return_list(PostCommentSerializer, PostComments, post.pk)
            likes = return_list(PostLikeSerializer, PostLikes, post.pk)
            shares = return_list(PostShareSerializer, PostShare, post.pk)
            tags = return_list(PostTagSerializer, PostTag, post.pk)
            arr_2 = [post, media, comments, likes, shares, tags]
            arr.append(arr_2)
            # user = UserSerializer, User, post.user)
            # import pdb
            # pdb.set_trace()
            # media = PostMedia.objects.filter(post=post.pk)
            # comments = PostComments.objects.filter(post=post.pk)
            #
            # likes = PostLikes.objects.filter(post=post.pk)
            # shares = PostShare.objects.filter(post=post.pk)
            # tags = PostTag.objects.filter(post=post.pk)
        # print(arr)
        import pdb
        pdb.set_trace()
        return arr

    # @api_view(['GET'])
    # def get_queryset(self):
    #     # import pdb
    #     # pdb.set_trace()
    #     posts = Post.objects.filter(user=self.request.user.id)
    #     for post in queryset:
    #         post = post
    #         media = PostMedia.objects.filter(post=post.pk)
    #         comments = PostComments.objects.filter(post=post.pk)
    #         likes = PostLikes.objects.filter(post=post.pk)
    #         shares = PostShare.objects.filter(post=post.pk)
    #         tags = PostTag.objects.filter(post=post.pk)
    #
    #     return queryset
    #     # queryset = Post.objects.all()
    #     # return queryset
