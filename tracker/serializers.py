from rest_framework import serializers
from .models import Unit, Visit


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ['id', 'name']


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['id', 'date_time', 'unit', 'latitude', 'longitude']

    def to_representation(self, instance):
        """
        Customize the representation of the Visit model.
        Only include the date_time and visit fields in the response.
        """
        representation = super().to_representation(instance)
        return {
            'visit': representation['id'],
            'date_time': representation['date_time']
        }