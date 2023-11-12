from rest_framework import permissions
from rest_framework.views import View


class HaveStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.role != 'hospede':
            return True

        return False
