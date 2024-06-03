from rest_framework import serializers
from companyprofile.models import Service, Company, Industry, Events, News, Leads, Scheme


class ServiceSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Service
        fields = ['id','company_name', 'name', 'short_description', 'long_description', 'created_at']

    

class CompanySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.email', read_only=True)
    industry_name = serializers.CharField(source='industry.name', read_only=True)

    class Meta:
        model = Company
        fields = ['id','created_by_name', 'industry_name', 'name', 'email', 'number', 'gst_number', 'reg_number', 'reg_date', 'sector', 'description', 'address', 'created_at','is_verify' ]

        


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Industry
        fields='__all__'  
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'
  
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'
        
class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Scheme
        fields='__all__'
        
class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leads
        fields='__all__'


class VerifyCompanySerializer(serializers.Serializer):
    company_id = serializers.IntegerField()
    is_verify = serializers.BooleanField()
