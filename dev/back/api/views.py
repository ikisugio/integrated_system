from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import OfficeSerializer
from .models import Office


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer