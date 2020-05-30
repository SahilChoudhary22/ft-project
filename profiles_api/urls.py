from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# instantiate router
router = DefaultRouter()
# register profile in router
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # since UserActivity is an APIview, it's not routed and instead added to urlpatterns
    path('user-activity/', views.UserActivity.as_view(), name='user-activity-list'),
]
