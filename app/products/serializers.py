from rest_framework import serializers
from .models import Cars


class CarsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'