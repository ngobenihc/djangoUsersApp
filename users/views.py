from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets

from users.serializer import UserSerializer


# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer