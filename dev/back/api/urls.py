from django.urls import path, include
from rest_framework import routers
from api.views import OfficeViewSet


router = routers.DefaultRouter()
router.register('office', OfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]