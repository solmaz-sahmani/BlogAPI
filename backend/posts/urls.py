from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
