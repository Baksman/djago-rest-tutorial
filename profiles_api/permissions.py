from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit users own profile"""


    def has_object_permission(self,request,view,obj):
        """check if user is trying to update thee own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
