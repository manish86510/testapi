from rest_framework import serializers
from Auth.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city_name', 'city_code')
