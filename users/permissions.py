from rest_framework import permissions
from rest_framework.views import View
from .models import User


class HaveStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.user.role != 'hospede' and (request.method in permissions.SAFE_METHODS):
            return True

        return False


class StaffOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.user.role != 'hospede':
            return True

        return request.user.is_authenticated and obj == request.user
