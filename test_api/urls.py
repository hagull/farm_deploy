from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()

router.register('post', PostViewSet)
app_name = 'test_api'
urlpatterns = [
    path('api/', include(router.urls))
]