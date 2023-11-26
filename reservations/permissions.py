from rest_framework import permissions
from rest_framework.views import View
from .models import Reservation


class StaffOrOwnerReservationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Reservation):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.user.role != 'hospede':
            return True

        return request.user.is_authenticated and obj.guest == request.user
