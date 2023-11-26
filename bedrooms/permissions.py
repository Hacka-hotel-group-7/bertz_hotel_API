from rest_framework import permissions
from rest_framework.views import View


class HasSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view: View):
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False
