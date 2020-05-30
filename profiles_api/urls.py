from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('members', views.UserViewSet)
router.register('activity', views.ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
