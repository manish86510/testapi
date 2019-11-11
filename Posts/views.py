from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
import base64

from .serializers import *
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


# Added CreatePostView to create post from serializer data
class CreatePostView(APIView):
    model = Post
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        pk = request.POST.get('id')
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(user_id=pk)
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def put(self, request):
        pk = int(request.POST.get('id', ''))
        saved_places = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(places_saved.about_post)})

    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(Post.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = Post.objects.all()
        serializer = PostSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})


class PostLikesView(APIView):
    model = PostLikes
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        pk = request.POST.get('id')
        serializer_class = PostLikesSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def put(self, request):
        pk = int(request.POST.get('id', ''))
        saved_places = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostLikesSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(places_saved.post)})

    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(Post.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = Post.objects.all()
        serializer = PostLikesSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})


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
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def put(self, request):
        pk = int(request.POST.get('id', ''))
        saved_places = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostCommentsSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(places_saved.post)})

    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(Post.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = Post.objects.all()
        serializer = PostCommentsSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})


class PostShareView(APIView):
    model = PostShare
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, format=None):
        pk = request.POST.get('id')
        serializer_class = PostShareSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(post_id=pk)
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def put(self, request):
        pk = int(request.POST.get('id', ''))
        saved_places = get_object_or_404(Post.objects.all(), pk=pk)
        serializer = PostShareSerializer(instance=saved_places, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            places_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(places_saved.about)})

    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(Post.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "Post with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        place = Post.objects.all()
        serializer = PostShareSerializer(place, many=True)
        return Response({"MyPlace": serializer.data})


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
            return Response("Saved Successfully", status=HTTP_200_OK)
        else:
            return Response("Something is wrong", status=HTTP_200_OK)

    def put(self, request):
        pk = request.POST.get('post')
        posts = get_object_or_404(PostMedia.objects.all(), pk=pk)
        serializer = PostMediaSerializer(instance=posts, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            media_saved = serializer.save()
        return Response({"success": "Post '{}' updated successfully".format(media_saved.post)})

    def delete(self, request):
        pk = request.POST.get('id')
        place = get_object_or_404(PostMedia.objects.all(), pk=pk)
        place.delete()
        return Response({"message": "Media with id {} has been deleted.".format(pk)}, status=204)

    def get(self, instance):
        media = PostMedia.objects.all()
        serializer = PostMediaSerializer(media, many=True)
        return Response({"PostMedia": serializer.data})
