from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView
from accountio.models import CompanyProfile
from accountio.rest.serializers.company import CompanyProfileSerializer

class CompanyProfileCreateView(CreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileDetailView(RetrieveAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    lookup_field = 'pk'
