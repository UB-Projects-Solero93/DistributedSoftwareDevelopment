from rest_framework import permissions

from mediacloud.models import Comment


class IsAdminOrCommentExpert(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS and request.method != 'POST':
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_superuser or (
        obj == Comment and ('mediacloud.write_comments' in request.user.get_all_permissions()))


class IsExpertOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS and request.method != 'OPTIONS':
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return ('mediacloud.write_comments' in request.user.get_all_permissions())


class IsExpertAndSelfOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return ('mediacloud.write_comments' in request.user.get_all_permissions())
