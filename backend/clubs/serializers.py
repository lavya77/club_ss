from rest_framework import serializers
from .models import Club , Clubtype ,Membership ,Event ,Announcements
class ClubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Clubtype
        fields='__all__'
        
class ClubSerializer(serializers.ModelSerializer):
    Club = ClubtypeSerializer(read_only=True)
    class Meta:
        model = Club
        fields='__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'
class AnnouncementsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Announcements
        fields='__all__'
class MemebershipSerializer(serializers.ModelSerializer):
    class Meta:
        model=Membership
        fields ="__all__"              

    

