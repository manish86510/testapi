from rest_framework import serializers
from Auth.models import MyPlaces


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPlaces
        fields = ("place_name", "lat_long", "from_date", "to_date")
