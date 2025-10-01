from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsClubHeadOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.role == "Club Head" or request.user.is_superuser
