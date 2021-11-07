from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        is_customer = request.user.customer.first()
        print(is_customer, bool(is_customer))

        return bool(is_customer)
