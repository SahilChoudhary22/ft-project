from django.shortcuts import render
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ActivityPeriodSerializer
    queryset = models.ActivityPeriod.objects.all()
    