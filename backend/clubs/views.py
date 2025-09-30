from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Club , Clubtype ,Membership ,Event ,Announcements
from .serializers import (ClubSerializer,ClubtypeSerializer,MemebershipSerializers,EventSerialzer,AnnouncementsSerializers)

class ClubViewset(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class=ClubSerializer
    permission_classes = [IsAuthenticated]

class ClubtypeViewset(viewsets.ModelViewSet):
    queryset= Clubtype.objects.all()
    serializer_class=ClubtypeSerializer
    
class Eventviewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializers_class=EventSerialzer

class MembershipViewset(viewsets.ModelViewSet):
    queryset=Membership.objects.all()
    serializer_class=MemebershipSerializers

class AnnouncemntsViewset(viewsets.ModelViewSet):
    queryset=Announcements.objects.all()
    serializer_class=AnnouncementsSerializers
        
