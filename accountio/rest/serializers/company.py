from rest_framework import serializers
from accountio.models import CompanyProfile


class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = ['name', 'email', 'phone_number', 'address', 'description']

    def validate(self, attrs):
        user = self.context['request'].user
        if CompanyProfile.objects.filter(company_user=user).exists():
            raise serializers.ValidationError('you can create only one company')
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        organization = CompanyProfile.objects.create(company_user=user, **validated_data)
        return organization
