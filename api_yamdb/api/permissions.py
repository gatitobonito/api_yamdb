# from rest_framework import permissions
#
#
# class IsAuthorOrNot(permissions.BasePermission):
#     message = 'Вносить изменения может только автор'
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.author == request.user