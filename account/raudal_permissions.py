from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSuperUserOrSelfUser(BasePermission):

    def has_permission(self, request: Request, view):
        return bool(request.user and (request.user.is_staff or request.user.id == view.kwargs['pk']))
