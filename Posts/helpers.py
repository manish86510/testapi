from .models import *
from Posts.serializers.post import PostSerializer
from Posts.serializers.post_media import PostMediaSerializer
from Posts.serializers.post_comments import PostCommentSerializer
from Posts.serializers.post_likes import PostLikeSerializer
from Posts.serializers.post_share import PostShareSerializer
from Posts.serializers.post_tag import PostTagSerializer
from Auth.serializers.user import UserSerializer

def modify_input_for_multiple_files(property_id, image, type):
    dict = {}
    dict['post'] = property_id
    dict['file'] = image
    dict['file_type'] = type
    return dict


def return_list(serializer_name, model_name, post_key):
    data_objects = model_name.objects.filter(post=post_key)
    obj_data = []
    for object in data_objects:
        object_serializer = serializer_name(data=object)
        obj_data.append(object_serializer.initial_data)
    return obj_data
