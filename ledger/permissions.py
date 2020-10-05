from rest_framework.permissions import BasePermission


class TransactionPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin():
            return True

        return request.user.id == obj.created_by_id
