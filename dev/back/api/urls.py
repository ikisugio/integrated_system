from django.urls import path, include
from rest_framework import routers
from api.views import OfficeViewSet


router = routers.DefaultRouter()
router.register('offices', OfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]