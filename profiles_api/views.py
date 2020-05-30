#from django.shortcuts import render
from profiles_api import serializers
#from profiles_api import models
from profiles_api.models import UserProfile
from rest_framework import viewsets, filters
#from rest_framework.response import Response
#from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions
#from datetime import datetime
from profiles_api.serializers import GetUserActivitySerializer, UserProfileSerializer
import json

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # authentication type
    permission_classes = (permissions.UpdateOwnProfile,) # check permission
    filter_backends = (filters.SearchFilter,) # add filter
    search_fields = ('name', 'name', 'email',) # make it searchable by which fields


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # enable token in browsable api

class UserActivity(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = GetUserActivitySerializer
    

    

# class UserActivity(views.APIView):
#     def get(self, request):
#         """
#         :param request: request object
#                 QueryParams:
#                     :user_id - Valid User id (Optional
#                     :page - Page Number
#                     :page_size - No. of objects in the result
#         :return:
#         """
#         try:
#             user_id = request.GET.get('user_id', None)
#             page_number = request.GET.get('page', 1)
#             page_size = int(request.GET.get('page_size', 10))
            
#             if user_id is None:
#                 users = UserProfile.objects.filter(is_superuser=False).order_by('name')
#             else:
#                 try:
#                     users = UserProfile.objects.filter(id=user_id).order_by('name')
#                 except Exception as e:
#                     return Utils.dispatch_failure(request, INVALID_USER_ID)
#                 if len(users) == 0:
#                     return Utils.dispatch_failure(request, INVALID_USER_ID)
            
#             if page_size in PageSize.__members__.values():
#                 paginator = Paginator(users, page_size)
#                 total_pages = paginator.num_pages
#                 if total_pages >= paginator.num_pages:
#                     paginated_query_set = paginator.page(page_number)
#                     serializer = GetUserActivitySerializer(paginated_query_set, many=True)
#                 else:
#                     return Utils.dispatch_failure(request, PAGE_NOT_FOUND)
                
#                 page_data = {
#                     'page': {
#                         'current_page': page_number,
#                         'total_pages': total_pages
#                     }
                    
#                 }
#                 return Utils.dispatch_sucess(request, serializer.data, **page_data)
#             else:
#                 return Utils.dispatch_failure(request, INVALID_PAGE_SIZE)
#         except Exception as e:
#             print(e)
#             return Utils.dispatch_failure(request, INTERNAL_SERVER_ERROR)
    
#     def post(self, request):
#         try:
#             data = request.data
#             if isinstance(data, dict):
#                 start_time = data.get('start_time', None)
#                 end_time = data.get('end_time', None)
#                 user_id = data.get('user_id', None)
                
#                 if user_id is None or end_time is None or start_time is None:
#                     return Utils.dispatch_failure(request, INVALID_PARAMETER)
#                 user = UserProfile.objects.filter(id=user_id)
#                 if len(user) == 0:
#                     return Utils.dispatch_failure(request, INVALID_USER_ID)
#                 user = user.first()
#                 try:
#                     activity = {
#                         'start_time': json.dumps(start_time, indent=4, sort_keys=True, default=str),
#                         'end_time': json.dumps(end_time, indent=4, sort_keys=True, default=str),#datetime.strptime(end_time, INPUT_DATE_FORMAT),
#                         'user': user.id
#                     }
#                     # json.dumps(activity, indent=4, sort_keys=True, default=str
#                     serializer = serializers.CreateActivitySerializer(data=activity)
#                     if serializer.is_valid():
#                         serializer.save()
#                         return Utils.dispatch_sucess(request, None)
#                     else:
#                         return Utils.dispatch_failure(request, VALIDATION_ERROR, serializer.errors)
#                 except Exception as e:
#                     print(e)
#                     return Utils.dispatch_failure(request, INVALID_PARAMETER)
#             else:
#                 return Utils.dispatch_failure(request, INVALID_PARAMETER)
#         except Exception as e:
#             print(e)
#             return Utils.dispatch_failure(request, INTERNAL_SERVER_ERROR)


# class UserManagement(views.APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             try:
#                 user_data = {
#                     "name": data['name'],
#                     "email": data['email'],
#                     "tz": data['tz'],
#                 }
#                 serializer = serializers.CreateUserSerializer(data=user_data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Utils.dispatch_sucess(request, serializer.data)
#                 else:
#                     return Utils.dispatch_failure(request, VALIDATION_ERROR, serializer.errors)
#             except Exception as e:
#                 print(e)
#                 return Utils.dispatch_failure(request, INVALID_PARAMETER)
#         except Exception as e:
#             print(e)
#             return Utils.dispatch_failure(request, INTERNAL_SERVER_ERROR)
    
#     def get(self, request):
#         try:
#             users = UserProfile.objects.filter(is_superuser=False).order_by('name')
#             page = int(request.GET.get('page', 1))
#             page_size = int(request.GET.get('page_size', 10))
#             if page_size in PageSize.__members__.values():
#                 paginator = Paginator(users, page_size)
#                 total_pages = paginator.num_pages
#                 if total_pages >= paginator.num_pages:
#                     paginated_query_set = paginator.page(page)
#                     serializer = GetUserSerializer(paginated_query_set, many=True)
#                 else:
#                     return Utils.dispatch_failure(request, PAGE_NOT_FOUND)
#                 page_data = {
#                     'page': {
#                         'current_page': page,
#                         'total_pages': total_pages
#                     }
                    
#                 }
#                 return Utils.dispatch_sucess(request, serializer.data, **page_data)
#             else:
#                 return Utils.dispatch_failure(request, INVALID_PAGE_SIZE)
#         except Exception as e:
#             print(e)
#             return Utils.dispatch_failure(request, INTERNAL_SERVER_ERROR)