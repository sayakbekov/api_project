from django.shortcuts import render
from .models import Category, Nout
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, NoutSerializer
from rest_framework import permissions


class CategoryView(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]


class NoutView(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Nout.objects.all()
    serializer_class = NoutSerializer
    permission_classes = [
        permissions.AllowAny
    ]
