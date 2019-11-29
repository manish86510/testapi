from rest_framework import serializers
from Auth.models import MyPlaces


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = ("id", "place_name", "lat_long", "from_date", "to_date", 'user')
        # fields = "__all__"


class PlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = ("id", "place_name", "lat_long", "from_date", "to_date")
        # fields = "__all__"
