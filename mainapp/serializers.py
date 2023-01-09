from rest_framework import serializers
from .models import Category, Nout


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nout
        fields = '__all__'
