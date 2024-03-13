from django.urls import path, include
from accountio.rest.views import registration_login

app_name = 'accountio'

urlpatterns = [
    path('re',registration_login.OrganizationRegisterCreateView.as_view(), name='create')
]
