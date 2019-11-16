# from django.shortcuts import render
# from rest_framework import viewsets, generics
# import base64
# from Auth.models import *
# from django.views.decorators.http import require_http_methods
# from django.db.models.signals import post_save, post_delete
from rest_framework.generics import get_object_or_404
from .serializers import *
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser
from rest_framework.decorators import parser_classes, action


# Added CreatePostView to create post from serializer data
class CreatePostView(APIView):
    model = Post
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Post Create"],
        operation_summary="Creates a New Post",
        operation_description="Creates post using the details provided by the user",
        query_serializer=PostSerializer,
        responses={
            200: PostSerializer,
        }
    )
    def post(self, request, format=None):
        ui = request.user.id
        serializer_class = PostSerializer(data=request.data)
        import pdb
        pdb.set_trace()
        if serializer_class.is_valid():
            serializer_class.save(user_id=ui)
            return Response("Post Created Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong, Unable to create a post", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Post Create"],
        operation_summary="Updates an existing Post",
        operation_description="Updates an existing post with details modified by the user.",
        query_serializer=PostSerializer,
        responses={
            200: PostSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_obj = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(post_obj.about_post)})

    @swagger_auto_schema(
        tags=["Post Create"],
        operation_summary="Deletes an existing Post",
        operation_description="Deletes a previously created post based on the post id.",
        query_serializer=PostSerializer,
        responses={
            200: PostSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(Post.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(
        tags=["Post Create"],
        operation_summary="Displays all the Posts of current user",
        operation_description="Displays all the posts created by the current user",
        query_serializer=PostSerializer,
        responses={
            200: PostSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        myposts = Post.objects.filter(user=ui)
        serializer = PostSerializer(myposts, many=True)
        return Response({"Posts": serializer.data})


@parser_classes([FormParser, MultiPartParser])
class PostMediaView(APIView):
    model = PostMedia
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Media"],
        operation_summary="Create New Media Entry",
        operation_description="Creates a new media entry when any new media is uploaded for a post",
        request_body=PostMediaSerializer,
        responses={
            200: PostMediaSerializer,
        }
    )
    def post(self, request, format=None):
        pk = request.POST.get('post')
        serializer_class = PostMediaSerializer(data=request.data)
        import pdb
        pdb.set_trace()
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            return Response("Media Uploaded Successfully", status=HTTP_200_OK)
        else:
            return Response("Cannot Upload Media", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Posts Media"],
        operation_summary="Update an Existing Media",
        operation_description="Updates an existing media based on the `id` in the media table",
        responses={
            200: PostMediaSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        posts = get_object_or_404(PostMedia.objects.all(), pk=pk)
        serializer = PostMediaSerializer(instance=posts, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            media_saved = serializer.save()
        return Response({"success": "Post '{}' with media is updated successfully".format(media_saved.post)})

    @swagger_auto_schema(
        tags=["Posts Media"],
        operation_summary="Get all Media",
        operation_description="Delete a media entry from the table using the `id`",
        responses={
            200: PostMediaSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(PostMedia.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Media with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(
        tags=["Posts Media"],
        operation_summary="Get all Media added by current user",
        operation_description="Get all the information for every uploaded media for current user's posts",
        responses={
            200: PostMediaSerializer,
        }
    )
    def get(self, instance):
        result = set()
        ui = instance.user.id
        post_num = Post.objects.filter(user=ui)
        for x in post_num:
            media = PostMedia.objects.filter(post=x.id)
            for y in media:
                serializer = PostMediaSerializer(data=y.__dict__)
                import pdb
                pdb.set_trace()
                if serializer.is_valid(raise_exception=True):
                    result.add(serializer.data)
        if result:
            return Response({"PostMedia": result})


class PostCommentsView(APIView):
    model = PostComments
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Comments"],
        operation_summary="Create New Comment",
        operation_description="Creates a new comment over a post by `id` from the post table",
        query_serializer=PostCommentsSerializer,
        responses={
            200: PostCommentsSerializer,
        }
    )
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

    @swagger_auto_schema(
        tags=["Posts Comments"],
        operation_summary="Update an existing Comment",
        operation_description="Updates a comment based on the `id` from the comments table",
        query_serializer=PostCommentsSerializer,
        responses={
            200: PostCommentsSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostCommentsSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comments_saved = serializer.save()
        return Response({"success": "Comment '{}' updated successfully".format(comments_saved.post)})

    @swagger_auto_schema(
        tags=["Posts Comments"],
        operation_summary="Delete a Comment",
        operation_description="Delete a comment using the `id` from the comments table",
        query_serializer=PostCommentsSerializer,
        responses={
            200: PostCommentsSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        saved_comments = get_object_or_404(PostComments.objects.all(), id=pk)
        post_name = saved_comments.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_comments.delete()
        return Response({"message": "Comment with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(
        tags=["Posts Comments"],
        operation_summary="Get list of Comments from the current user",
        operation_description="Get all comments posted by current user",
        query_serializer=PostCommentsSerializer,
        responses={
            200: PostCommentsSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        comments = PostComments.objects.filter(user=ui)
        serializer = PostCommentsSerializer(comments, many=True)
        return Response({"Comments": serializer.data})


class PostShareView(APIView):
    model = PostShare
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Shared"],
        operation_summary="New Shared Post",
        operation_description="Creates a new share of a post using the `id` fetched from the post table",
        query_serializer=PostShareSerializer,
        responses={
            200: PostShareSerializer,
        }
    )
    def post(self, request, format=None):
        pk = request.POST.get('post')
        ui = request.user
        serializer_class = PostShareSerializer(data=request.data)
        import pdb
        pdb.set_trace()
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk, shared_by=ui)
            post_name = serializer_class.instance.post
            post_obj = Post.objects.get(about_post=post_name)
            post_obj.share_count += 1
            post_obj.save()
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    @swagger_auto_schema(
        tags=["Posts Shared"],
        operation_summary="Update Shared Posts",
        operation_description="Updates the information about a shared post using the `id` from the shared post table",
        query_serializer=PostShareSerializer,
        responses={
            200: PostShareSerializer,
        }
    )
    def put(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), pk=pk)
        serializer = PostShareSerializer(instance=saved_shares, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            shares_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(shares_saved.about)})

    @swagger_auto_schema(
        tags=["Posts Shared"],
        operation_summary="Delete a Shared Post",
        operation_description="Delete the information about a shared post based on the `id` of the shared post"
                              + " inside the database",
        query_serializer=PostShareSerializer,
        responses={
            200: PostShareSerializer,
        }
    )
    def delete(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), id=pk)
        post_name = saved_shares.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_shares.delete()
        return Response({"message": "Shared Post with id {} has been deleted.".format(pk)}, status=204)

    @swagger_auto_schema(
        tags=["Posts Shared"],
        operation_summary="Get Shared Posts of Current User",
        operation_description="Get the information of all the posts shared by the current user",
        query_serializer=PostShareSerializer,
        responses={
            200: PostShareSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        shares = PostShare.objects.filter(shared_by=ui)
        serializer = PostShareSerializer(shares, many=True)
        return Response({"Shared Posts": serializer.data})


class PostLikesView(APIView):
    model = PostLikes
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Post Likes"],
        operation_summary="Create a New Like",
        operation_description="Create a new like on a post",
        query_serializer=PostLikesSerializer,
        responses={
            200: PostLikesSerializer,
        }
    )
    def post(self, request, format=None):
        pk = request.POST.get('post')
        ui = request.user.id
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

    @swagger_auto_schema(
        tags=["Post Likes"],
        operation_summary="Delete a Like",
        operation_description="Delete a like based on the `id` from the user table and `id` of the "
                              + "post from the post table",
        query_serializer=PostLikesSerializer,
        responses={
            200: PostLikesSerializer,
        }
    )
    def delete(self, request):
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

    @swagger_auto_schema(
        tags=["Post Likes"],
        operation_summary="Get current user Likes",
        operation_description="Get current user's likes",
        query_serializer=PostLikesSerializer,
        responses={
            200: PostLikesSerializer,
        }
    )
    def get(self, instance):
        ui = instance.user.id
        likes = PostLikes.objects.filter(user=ui)
        serializer = PostLikesSerializer(likes, many=True)
        return Response({"MyLikes": serializer.data})


# GetAll methods defined separately to allow viewing of these methods in the documentation view.
# Separate declaration also allows to identify and disable these methods individually as these
# does not have any dependency over the requests passed to the views.
class GetAllPostsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Post Create"],
        operation_summary="Displays all the Posts",
        operation_description="Displays all the posts created till now.",
        query_serializer=PostSerializer,
        responses={
            200: PostSerializer,
        }
    )
    def get(self, instance):
        myposts = Post.objects.all()
        serializer = PostSerializer(myposts, many=True)
        return Response({"Posts": serializer.data})


class GetAllMediaView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Media"],
        operation_summary="Get all Media",
        operation_description="Get all the information for every uploaded media for all the posts",
        responses={
            200: PostMediaSerializer,
        }
    )
    def get(self, instance):
        media = PostMedia.objects.all()
        serializer = PostMediaSerializer(media, many=True)
        return Response({"PostMedia": serializer.data})


class GetAllCommentsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Comments"],
        operation_summary="Get all Comments",
        operation_description="Get all comments over all the posts",
        query_serializer=PostCommentsSerializer,
        responses={
            200: PostCommentsSerializer,
        }
    )
    def get(self, instance):
        comments = PostComments.objects.all()
        serializer = PostCommentsSerializer(comments, many=True)
        return Response({"Comments": serializer.data})


class GetAllSharesView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Posts Shared"],
        operation_summary="Get all Shared Posts",
        operation_description="Get all the information of all the shared posts yet",
        query_serializer=PostShareSerializer,
        responses={
            200: PostShareSerializer,
        }
    )
    def get(self, instance):
        shares = PostShare.objects.all()
        serializer = PostShareSerializer(shares, many=True)
        return Response({"Shared Posts": serializer.data})


class GetAllLikesView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(
        tags=["Post Likes"],
        operation_summary="Get all the Likes",
        operation_description="Get all the likes present yet",
        query_serializer=PostLikesSerializer,
        responses={
            200: PostLikesSerializer,
        }
    )
    def get(self, instance):
        likes = PostLikes.objects.all()
        serializer = PostLikesSerializer(likes, many=True)
        return Response({"MyLikes": serializer.data})
