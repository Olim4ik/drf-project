from django.contrib.auth.models import Group

from rest_framework.permissions import BasePermission


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        """
        Takes a user and a group name, and returns `True` if the user is in that group.
        """
        # print(request.user.id)
        try:
            return Group.objects.get(name='subscribers').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return False



# from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsOwnerOrReadOnly(BasePermission):
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True

#         return obj.account == request.user


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user