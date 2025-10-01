from django.contrib import admin
from .models import Club, Clubtype, Membership, Event, Announcements

# ClubType Admin
@admin.register(Clubtype)
class ClubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'club_type')
    search_fields = ('club_type',)


# Club Admin
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'club_name', 'club', 'description')
    list_filter = ('club',)  # filter by club type
    search_fields = ('club_name', 'description')


# Event Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organised_by', 'date')
    list_filter = ('organised_by',)
    search_fields = ('name', 'description')
    ordering = ('date',)  # order by date


# Announcements Admin
@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Announcements_name', 'club_related')
    list_filter = ('club_related',)
    search_fields = ('Announcements_name', 'description')


# Membership Admin
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'club', 'role', 'date_joined')
    list_filter = ('club', 'role')
    search_fields = ('user__username', 'club__club_name')
