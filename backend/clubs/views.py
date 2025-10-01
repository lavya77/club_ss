from django.shortcuts import render
from .permissions import IsClubHeadOrReadOnly

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
    serializer_class=EventSerialzer
    permission_classes = [IsAuthenticated , IsClubHeadOrReadOnly]

    @action(detail=False, methods=["get"])
    def events(self,request , pk=None):
        club=self.get_object()
        events=Event.objects.filter(organised_by=club,date__gte=timezone)
        serializer =EventSerialzer(events,many =True)
        return Response(serializer.data)
    def get_queryset(self):
        user = self.request.user
        if user.role == "Club Head":
            return Event.objects.filter(organised_by=user.club)
        return Event.objects.all()
    def perform_create(self, serializer):
        user = self.request.user
        if user.role == "Club Head":
            serializer.save(organised_by=user.club)
        else:
            serializer.save()


class MembershipViewset(viewsets.ModelViewSet):
    queryset=Membership.objects.all()
    serializer_class=MemebershipSerializers

class AnnouncemntsViewset(viewsets.ModelViewSet):
    queryset=Announcements.objects.all()
    serializer_class=AnnouncementsSerializers

