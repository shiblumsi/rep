from rest_framework import permissions
from accountio.models import CompanyProfile
from deviceio.models import Department, Device, Employee
from django.shortcuts import get_object_or_404



class IsCompanyDepartment(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        department = get_object_or_404(Department, uuid=uuid)
        # Check if the logged-in user is the owner(company_user) of the department's company
        return request.user == department.company.company_user
    
    message = 'You do not have permission to access departments of other companies.'


class IsCompanyEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        employee = get_object_or_404(Employee, uuid=uuid)
        # Check if the logged-in user is the owner(company_user) of the employees company
        return request.user == employee.company.company_user
    
    message = 'You do not have permission to access employees of other companies.'


class IsCompanyDevice(permissions.BasePermission):
    def has_permission(self, request, view):
        uuid = view.kwargs.get('uuid')
        device = get_object_or_404(Device, uuid=uuid)
        # Check if the logged-in user is the owner(company_user) of the device's company
        return request.user == device.company.company_user
    
    message = 'You do not have permission to access devices of other companies.'