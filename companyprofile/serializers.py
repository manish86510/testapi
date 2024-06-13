from rest_framework import serializers
from companyprofile.models import Service, Company, Industry, Events, News, Leads, Scheme, Plan, Subscription, Apply, Ticket



class ServiceSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Service
        # fields = ['id','company_name', 'name', 'short_description', 'long_description', 'created_at']
        fields = ['company', 'company_name', 'id','name', 'short_description', 'long_description', 'created_at','banner']

    

class CompanySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.email', read_only=True)
    industry_name = serializers.CharField(source='industry.name', read_only=True)

    class Meta:
        model = Company
        fields = ['id','created_by_name', 'industry_name', 'name', 'email', 'banner','url','logo','number', 'gst_number', 'reg_number', 'reg_date', 'sector', 'description', 'address', 'created_at','is_verify' ]



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
    

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields='__all__'
        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscription
        fields='__all__'
        

class ApplySerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    company_logo = serializers.SerializerMethodField()
    class Meta:
        model = Apply
        fields = ['id', 'subject', 'description','company_name','company_logo', 'attachment', 'company','created_at', 'updated_at','user']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
        
    def get_company_name(self, obj):
        return obj.company.name

    def get_company_logo(self, obj):
        return obj.company.logo.url if obj.company.logo else None
    
    
class TicketSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'attachment', 'user_name', 'user_id', 'created_at', 'updated_at']

        
