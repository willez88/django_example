from rest_framework import serializers

from .models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='base:country-detail')

    class Meta:
        model = Country
        fields = ('url', 'name')
