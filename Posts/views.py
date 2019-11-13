from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
import base64
from Auth.models import *
from .serializers import *
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.db.models.signals import post_save, post_delete
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes, action


# Added CreatePostView to create post from serializer data
# @swagger_auto_schema(tags='CreatePost', query_serializer=PostSerializer, responses={200: PostSerializer})
class CreatePostView(APIView):
    model = Post
    @swagger_auto_schema(tags=["Post Create"], operation_summary="Creates a New Post", operation_description="Creates post using the details provided by the user", responses={200: PostSerializer})
    def post(self, request, format=None):
        pk = request.POST.get('user')
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(user_id=pk)
            return Response("Post Created Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong, Unable to create a post", status=HTTP_200_OK)

    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(tags=["Post Create"], operation_summary="Updates an existing Post", operation_description="Updates an existing post with details modified by the user.", responses={200: PostSerializer})
    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_obj = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(post_obj.about_post)})

    @swagger_auto_schema(tags=["Post Create"], operation_summary="Deletes an existing Post", operation_description="Deletes a previously created post based on the post id.", responses={200: PostSerializer})
    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(Post.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(tags=["Post Create"], operation_summary="Displays all the Posts", operation_description="Displays all the posts created till now.", responses={200: PostSerializer})
    def get(self, instance):
        myposts = Post.objects.all()
        serializer = PostSerializer(myposts, many=True)
        return Response({"Posts": serializer.data})

@parser_classes([FormParser, MultiPartParser])
class PostMediaView(APIView):
    model = PostMedia
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(tags=["Posts Media"], operation_summary="Create New Media Entry", operation_description="Creates a new media entry when any new media is uploaded for a post", responses={200: PostMediaSerializer})
    # @action(detail=False, methods=['post'])
    # @swagger_auto_schema(query_serializer=PostMediaSerializer, responses={200: PostMediaSerializer})
    def post(self, request, format=None):
        # import pdb
        # pdb.set_trace()
        pk = request.POST.get('post')
        serializer_class = PostMediaSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            return Response("Media Uploaded Successfully", status=HTTP_200_OK)
        else:
            return Response("Cannot Upload Media", status=HTTP_200_OK)

    @swagger_auto_schema(tags=["Posts Media"], operation_summary="Update an Existing Media", operation_description="Updates an existing media based on the `id` in the media table", responses={200: PostMediaSerializer})
    # @swagger_auto_schema(tags='PostMedia', query_serializer=PostMediaSerializer, responses={200: PostMediaSerializer})
    def put(self, request):
        pk = request.POST.get('id')
        posts = get_object_or_404(PostMedia.objects.all(), pk=pk)
        serializer = PostMediaSerializer(instance=posts, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            media_saved = serializer.save()
        return Response({"success": "Post '{}' with media is updated successfully".format(media_saved.post)})

    @swagger_auto_schema(tags=["Posts Media"], operation_summary="Get all Media", operation_description="Delete a media entry from the table using the `id`", responses={200: PostMediaSerializer})
    # @swagger_auto_schema(tags='PostMedia', query_serializer=PostMediaSerializer, responses={200: PostMediaSerializer})
    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(PostMedia.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Media with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(tags=["Posts Media"], operation_summary="Get all Media", operation_description="Get all the information for every uploaded media for all the posts", responses={200: PostMediaSerializer})
    # @swagger_auto_schema(query_serializer=PostMediaSerializer, responses={200: PostMediaSerializer})
    def get(self, instance):
        media = PostMedia.objects.all()
        serializer = PostMediaSerializer(media, many=True)
        return Response({"PostMedia": serializer.data})


# @swagger_auto_schema(tags=["Posts Comments"] ,query_serializer=PostCommentsSerializer, responses={200: PostCommentsSerializer})
# @action(detail=False, methods=["GET", "POST", "DELETE", "PUT"])
class PostCommentsView(APIView):
    model = PostComments
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(tags=["Posts Comments"], operation_summary="Create New Comment", operation_description="Creates a new comment over a post by `id` from the post table", responses={200: PostCommentsSerializer})
    # @swagger_auto_schema(query_serializer=PostCommentsSerializer, responses={200: PostCommentsSerializer})
    # @action(detail=False, method=["POST"])
    def post(self, request, format=None):
        pk = request.POST.get('id')
        serializer_class = PostCommentsSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            post_name = serializer_class.instance.post
            post_obj = Post.objects.get(about_post=post_name)
            post_obj.share_count += 1
            post_obj.save()
            return Response("Comment Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Cannot add comment", status=HTTP_200_OK)

    @swagger_auto_schema(tags=["Posts Comments"], operation_summary="Update an existing Comment", operation_description="Updates a comment based on the `id` from the comments table", responses={200: PostCommentsSerializer})
    # @swagger_auto_schema(query_serializer=PostCommentsSerializer, responses={200: PostCommentsSerializer})
    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostCommentsSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comments_saved = serializer.save()
        return Response({"success": "Comment '{}' updated successfully".format(comments_saved.post)})

    @swagger_auto_schema(tags=["Posts Comments"], operation_summary="Delete a Comment", operation_description="Delete a comment using the `id` from the comments table", responses={200: PostCommentsSerializer})
    # @swagger_auto_schema(query_serializer=PostCommentsSerializer, responses={200: PostCommentsSerializer})
    def delete(self, request):
        pk = request.POST.get('id')
        saved_comments = get_object_or_404(PostComments.objects.all(), id=pk)
        post_name = saved_comments.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_comments.delete()
        return Response({"message": "Comment with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(tags=["Posts Comments"], operation_summary="Get all Comments", operation_description="Get all comments over all the posts", responses={200: PostCommentsSerializer})
    # @swagger_auto_schema(query_serializer=PostCommentsSerializer, responses={200: PostCommentsSerializer})
    def get(self, instance):
        comments = PostComments.objects.all()
        serializer = PostCommentsSerializer(comments, many=True)
        return Response({"Comments": serializer.data})


class PostShareView(APIView):
    model = PostShare
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(tags=["Posts Shared"], operation_summary="New Shared Post", operation_description="Creates a new share of a post using the `id` fetched from the post table", responses={200: PostShareSerializer})
    def post(self, request, format=None):
        pk = request.POST.get('post')
        serializer_class = PostShareSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            post_name = serializer_class.instance.post
            post_obj = Post.objects.get(about_post=post_name)
            post_obj.share_count += 1
            post_obj.save()
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    @swagger_auto_schema(tags=["Posts Shared"], operation_summary="Update Shared Posts", operation_description="Updates the information about a shared post using the `id` from the shared post table", responses={200: PostShareSerializer})
    def put(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), pk=pk)
        serializer = PostShareSerializer(instance=saved_shares, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            shares_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(shares_saved.about)})

    @swagger_auto_schema(tags=["Posts Shared"], operation_summary="Delete a Shared Post", operation_description="Delete the information about a shared post based on the `id` of the shared post inside the database", responses={200: PostShareSerializer})
    def delete(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), id=pk)
        post_name = saved_shares.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_shares.delete()
        return Response({"message": "Shared Post with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(tags=["Posts Shared"], operation_summary="Get all Shared Posts", operation_description="Get all the information of all the shared posts yet", responses={200: PostShareSerializer})
    def get(self, instance):
        shares = PostShare.objects.all()
        serializer = PostShareSerializer(shares, many=True)
        return Response({"Shared Posts": serializer.data})


class PostLikesView(APIView):
    model = PostLikes
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(tags=["Post Likes"], operation_summary="Create a New Like", operation_description="Create a new like on a post", responses={200: PostLikesSerializer})
    def post(self, request, format=None):
        pk = request.POST.get('post')
        ui = request.POST.get('user')
        serializer_class = PostLikesSerializer(data=request.data)
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

    # @swagger_auto_schema(tags=["Post Likes"], operation_summary="Update an Existing Like", operation_description="Update a like based on id of the like entry", responses={200: PostLikesSerializer})
    # def put(self, request):
    #     pk = request.POST.get('id')
    #     saved_likes = get_object_or_404(PostLikes.objects.all(), pk=pk)
    #     serializer = PostLikesSerializer(instance=saved_likes, data=request.data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         likes_saved = serializer.save()
    #     return Response({"success": "Likes '{}' updated successfully".format(likes_saved.post)})

    @swagger_auto_schema(tags=["Post Likes"], operation_summary="Delete a Like", operation_description="Delete a like based on the `id` from the user table and `id` of the post from the post table", responses={200: PostLikesSerializer})
    def delete(self, request):
        pk = request.POST.get('post')
        ui = request.POST.get('user')
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

    @swagger_auto_schema(tags=["Post Likes"], operation_summary="Get all the Likes", operation_description="Get all the likes present yet", responses={200: PostLikesSerializer})
    def get(self, instance):
        likes = PostLikes.objects.all()
        serializer = PostLikesSerializer(likes, many=True)
        return Response({"MyLikes": serializer.data})
