from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

# Create your models here.
class Clubtype(models.Model):
    club_type=models.CharField(max_length=200)

    def __str__ (self):
        return self.club_type
    
class Club(models.Model):
    club_name=models.CharField(max_length=200)
    club=models.ForeignKey(Clubtype,on_delete=models.CASCADE,related_name="clubs")
    description=models.TextField()

    def __str__(self):
        return self.club_name

class Event(models.Model):
    name=models.CharField(max_length=200)
    organised_by =models.ForeignKey(Club,on_delete=models.CASCADE)
    description = models.TextField()
    date=models.DateTimeField()
    venue=models.CharField(max_length=500)


    def __str__(self):
        self.name

class Announcements(models.Model):
    Announcements_name=models.CharField(max_length=500)
    description=models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    club_related=models.ForeignKey(Club,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Announcements_name

 
class Membership(models.Model):
    ROLE_CHOICES = [
        ("head", "Club Head"),
        ("member", "Member"),
        ("secretary", "Secretary"),
        ("treasurer", "Treasurer"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ForeignKey("Club", on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="member")

    def __str__(self):
        return f"{self.user} - {self.club} ({self.role})"
