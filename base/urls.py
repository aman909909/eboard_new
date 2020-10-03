from django.urls import path, include
from rest_framework import routers
from .views import BoardViewSet


router = routers.DefaultRouter()
router.register('boards', BoardViewSet)

urlpatterns = [
   path('', include(router.urls)),
]