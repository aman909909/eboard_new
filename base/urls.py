from django.urls import path, include
from rest_framework import routers
from .views import BoardViewSet, ListViewSet, CardViewSet


router = routers.DefaultRouter()
router.register('boards', BoardViewSet)
router.register('lists', ListViewSet)
router.register('cards', CardViewSet)

urlpatterns = [
   path('', include(router.urls)),
]