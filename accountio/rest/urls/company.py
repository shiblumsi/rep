from django.urls import path
from accountio.rest.views import company

app_name = 'accountio'

urlpatterns = [
    path('cc', company.CompanyProfileCreateView.as_view(), name='company-create-profile'),
    path('cd/<pk>', company.CompanyProfileDetailView.as_view(), name='company-detail-profile'),
]
