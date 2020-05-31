from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# instantiate router
router = DefaultRouter()
# register profiles and useractivity in router
router.register('profile', views.UserProfileViewSet, basename="profile")
router.register('user-activity', views.UserActivity)

urlpatterns = [
    path('', include(router.urls)),
    # path to login user and further allow them to modify their profile
    path('login/', views.UserLoginApiView.as_view()),
]
