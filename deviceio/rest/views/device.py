from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from deviceio.models import Department, Employee, Device, Checkout, ReturnLog
from .serializers import OrganizationSerializer, DeviceSerializer, CheckoutSerializer, EmployeeSerializer, \
    ReturnSerializer


class OrganizationCreate(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EmployeeCreate(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeviceCreate(CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class CheckoutCreate(CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class ReturnCreate(CreateAPIView):
    queryset = ReturnLog.objects.all()
    serializer_class = ReturnSerializer
