from profiles_api import serializers
from profiles_api.models import UserProfile
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions
from profiles_api.serializers import GetUserActivitySerializer, UserProfileSerializer
import json


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # authentication type
    permission_classes = (permissions.UpdateOwnProfile,) # check permission
    filter_backends = (filters.SearchFilter,) # add filter
    search_fields = ('id', 'name', 'email',) # specifying the fields that can be used to search the user


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # enable token in browsable api

class UserActivity(viewsets.ReadOnlyModelViewSet):
    """Handles the user activity"""
    queryset = UserProfile.objects.all()
    serializer_class = GetUserActivitySerializer