#from django.shortcuts import render
from rest_framework import viewsets
from themecampsapp.models import User,Camp,CampLocation,CampMember,CampSafety,Workshop
from themecampsapp.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer

class CampViewSet(viewsets.ModelViewSet):
    queryset = Camp.objects.all()
    serializer_class=CampSerializer

class CampLocationViewSet(viewsets.ModelViewSet):
    queryset = CampLocation.objects.all()
    serializer_class=CampLocationSerializer

class CampMemberViewSet(viewsets.ModelViewSet):
    queryset = CampMember.objects.all()
    serializer_class=CampMemberSerializer

class CampSafetyViewSet(viewsets.ModelViewSet):
    queryset = CampSafety.objects.all()
    serializer_class=CampSafetySerializer

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class=WorkshopSerializer
