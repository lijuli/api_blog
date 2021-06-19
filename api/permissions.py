from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def is_author_or_admin(self, request, obj):
        return (request.user == obj.author or
                request.user.is_staff or
                request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS or
            (request.method in ('DELETE', 'PATCH') and
             self.is_author_or_admin(request, obj))

        )


class AuthorCanDelete(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
                request.method == 'DELETE' or
                obj.author == request.user
        )



class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_staff)


class IsModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in
            permissions.SAFE_METHODS or request.user.is_staff
        )

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.is_superuser)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return(request.method in permissions.SAFE_METHODS
               or request.user.is_superuser)


