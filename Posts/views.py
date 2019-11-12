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


# Added CreatePostView to create post from serializer data
class CreatePostView(APIView):
    model = Post
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        pk = request.POST.get('user')
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(user_id=pk)
            return Response("Post Created Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong, Unable to create a post", status=HTTP_200_OK)

    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_obj = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(post_obj.about_post)})

    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(Post.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        myposts = Post.objects.all()
        serializer = PostSerializer(myposts, many=True)
        return Response({"Posts": serializer.data})


class PostMediaView(APIView):
    model = PostMedia
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        pk = request.POST.get('post')
        serializer_class = PostMediaSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            return Response("Media Uploaded Successfully", status=HTTP_200_OK)
        else:
            return Response("Cannot Upload Media", status=HTTP_200_OK)

    def put(self, request):
        pk = request.POST.get('post')
        posts = get_object_or_404(PostMedia.objects.all(), pk=pk)
        serializer = PostMediaSerializer(instance=posts, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            media_saved = serializer.save()
        return Response({"success": "Post '{}' with media is updated successfully".format(media_saved.post)})

    def delete(self, request):
        pk = request.POST.get('id')
        del_query = get_object_or_404(PostMedia.objects.all(), pk=pk)
        del_query.delete()
        return Response({"message": "Media with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        media = PostMedia.objects.all()
        serializer = PostMediaSerializer(media, many=True)
        return Response({"PostMedia": serializer.data})


class PostCommentsView(APIView):
    model = PostComments
    permission_classes = [
        IsAuthenticated,
    ]

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

    def put(self, request):
        pk = request.POST.get('id')
        instance_obj = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostCommentsSerializer(instance=instance_obj, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comments_saved = serializer.save()
        return Response({"success": "Comment '{}' updated successfully".format(comments_saved.post)})

    def delete(self, request):
        pk = request.POST.get('id')
        saved_comments = get_object_or_404(PostComments.objects.all(), id=pk)
        post_name = saved_comments.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_comments.delete()
        return Response({"message": "Comment with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        comments = PostComments.objects.all()
        serializer = PostCommentsSerializer(comments, many=True)
        return Response({"Comments": serializer.data})


class PostShareView(APIView):
    model = PostShare
    permission_classes = [
        IsAuthenticated,
    ]

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

    def put(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), pk=pk)
        serializer = PostShareSerializer(instance=saved_shares, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            shares_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(shares_saved.about)})

    def delete(self, request):
        pk = request.POST.get('id')
        saved_shares = get_object_or_404(PostShare.objects.all(), id=pk)
        post_name = saved_shares.post
        post_obj = Post.objects.get(about_post=post_name)
        post_obj.share_count -= 1
        post_obj.save()
        saved_shares.delete()
        return Response({"message": "Shared Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        shares = PostShare.objects.all()
        serializer = PostShareSerializer(shares, many=True)
        return Response({"Shared Posts": serializer.data})


class PostLikesView(APIView):
    model = PostLikes
    permission_classes = [
        IsAuthenticated,
    ]

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

    def put(self, request):
        pk = request.POST.get('id')
        saved_likes = get_object_or_404(PostLikes.objects.all(), pk=pk)
        serializer = PostLikesSerializer(instance=saved_likes, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            likes_saved = serializer.save()
        return Response({"success": "Likes '{}' updated successfully".format(likes_saved.post)})

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

    def get(self, instance):
        likes = PostLikes.objects.all()
        serializer = PostLikesSerializer(likes, many=True)
        return Response({"MyLikes": serializer.data})
