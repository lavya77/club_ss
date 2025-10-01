from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClubViewset,
    ClubtypeViewset,
    Eventviewset,
    MembershipViewset,
    AnnouncemntsViewset,
)
router =DefaultRouter()
router.register(r'clubs',ClubViewset,basename='club')
router.register(r'clubtypes', ClubtypeViewset, basename='clubtype')
router.register(r'events', Eventviewset, basename='event')
router.register(r'memberships', MembershipViewset, basename='membership')
router.register(r'announcements', AnnouncemntsViewset, basename='announcement')

urlpatterns = [
    path('', include(router.urls)),
]
