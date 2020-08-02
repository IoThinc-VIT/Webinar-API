from rest_framework import serializers
from .models import webinarsmodel

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=webinarsmodel
        fields='__all__'