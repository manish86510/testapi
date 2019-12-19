from rest_framework import viewsets
from ..serializers.follow import FollowerSerializer, FollowerCreateSerializer
from ..swagger.user_my_followers import FollowerSwagger, FollowingSwagger
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..models import Followers


@method_decorator(name='create', decorator=FollowerSwagger.create())
@method_decorator(name='destroy', decorator=FollowerSwagger.delete())
class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer

    http_method_names = ['post', 'delete']

    def create(self, request, *args, **kwargs):
        serializer = FollowerCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            follower = User.objects.get(pk=request.data.get('follower'))
            serializer.save(follower=follower, user=self.request.user)
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        query = Followers.objects.get(id=self.kwargs['pk'])
        query.deleted_on = timezone.now()
        query.delete()
        return Response("Deleted Successfully", status=status.HTTP_204_NO_CONTENT)


@method_decorator(name='list', decorator=FollowingSwagger.list())
@method_decorator(name='retrieve', decorator=FollowingSwagger.retrieve())
class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Followers.objects.filter(user=self.request.user)
        return queryset


@method_decorator(name='list', decorator=FollowerSwagger.list())
@method_decorator(name='retrieve', decorator=FollowerSwagger.retrieve())
class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class = FollowerSerializer

    http_method_names = ['get']

    def get_queryset(self):
        queryset = Followers.objects.filter(following=self.request.user)
        return queryset
