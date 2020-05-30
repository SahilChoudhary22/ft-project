from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """Check user is trying to edit their own profile only"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # if request isnt in the safe methods, 
        # we return whether the ID they are editing is their own
        return obj.id == request.user.id