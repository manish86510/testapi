
from rest_framework.decorators import api_view
from rest_framework.response import Response
from companyprofile.models import Company,Service, Apply, Ticket
from .serializers import ServiceSerializer,CompanySerializer,IndustrySerializer,EventsSerializer, NewsSerializer, SchemeSerializer ,LeadsSerializer, VerifyCompanySerializer, PlanSerializer, SubscriptionSerializer, ApplySerializer, TicketSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT,HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers
from .models import *
from Auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from django.db.models import Count
from datetime import date


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def verify_company(request):
    serializer = VerifyCompanySerializer(data=request.data)
    if serializer.is_valid():
        company_id = serializer.validated_data['company_id']
        is_verify = serializer.validated_data['is_verify']

        try:
            company = Company.objects.get(pk=company_id)
            company.is_verify = is_verify
            company.save()

            return Response({
                'message': f'Company {company.name} verification status updated',
                'is_verify': company.is_verify
            }, status=HTTP_200_OK)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'}, status=HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)




# Create your views here.
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['id', 'username', 'name', 'date_of_birth', 'email', 'is_active', 'date_joined']

# class GetUserFromToken(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user_data = request.user
#         serializer = CustomUserSerializer(user_data)
#         return Response({'data': serializer.data})

@api_view(['GET', 'POST'])
def service_list_view(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def service_detail_view(request, pk):
    if request.method == 'GET':
        try:
            service = Service.objects.get(pk=pk)
            serializer = ServiceSerializer(service)
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        try:
            service = Service.objects.get(pk=pk)
            service.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=HTTP_404_NOT_FOUND)
        
        



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_service_view(request):
    try:
        service = Service.objects.get(created_by=request.user)
        serializer = ServiceSerializer(service)
        return Response({"data": serializer.data}, status=HTTP_200_OK)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=HTTP_404_NOT_FOUND)








       


@api_view(['GET'])
def company_detail_view(request, service_pk):
    if request.method == 'GET':
        try:
            service = Service.objects.get(pk=service_pk)
            companies = Company.objects.filter(service=service)
            serializer = CompanySerializer(companies, many=True)
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=HTTP_404_NOT_FOUND)






@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def company_view(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                company = Company.objects.get(id=id)
            except Company.DoesNotExist:
                return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        else:
            companies = Company.objects.all().order_by('-created_at')
            serializer = CompanySerializer(companies, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        user = request.user  # Get the authenticated user from the token

        company_data = request.data.copy()
        company_data['created_by'] = user.id  # Store user's ID as created_by
        company_data['user'] = user.id  # Also store user's ID as user
        serializer = CompanySerializer(data=company_data)
        if serializer.is_valid():
            serializer.save(created_by=user, user=user)  # Set the created_by and user fields in the serializer
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    # elif request.method == 'PUT':
    #     try:
    #         company = Company.objects.get(pk=id)
    #     except Company.DoesNotExist:
    #         return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)
    #     serializer = CompanySerializer(company, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"data": serializer.data}, status=HTTP_200_OK)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_company_view(request):
    try:
        company = Company.objects.get(created_by=request.user)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)

    serializer = CompanySerializer(company)
    return Response(serializer.data, status=HTTP_200_OK)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def industry_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                industry = Industry.objects.get(pk=pk)
            except Industry.DoesNotExist:
                return Response({"error": "Industry not found"}, status=HTTP_404_NOT_FOUND)
            serializer = IndustrySerializer(industry)
            return Response({"data": serializer.data})
        else:
            industry = Industry.objects.all().order_by('-created_at')
            serializer = IndustrySerializer(industry, many=True)
            return Response({"data": serializer.data})

    elif request.method == 'POST':
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            industry = Industry.objects.get(pk=pk)
        except Industry.DoesNotExist:
            return Response({"error": "Industry not found"}, status=HTTP_404_NOT_FOUND)
        serializer = IndustrySerializer(industry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            industry = Industry.objects.get(pk=pk)
        except Industry.DoesNotExist:
            return Response({"error": "Industry not found"}, status=HTTP_404_NOT_FOUND)
        industry.delete()
        return Response({"message": "Industry deleted successfully"}, status=HTTP_204_NO_CONTENT)
    
 
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def events_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                events = Events.objects.get(pk=pk)
            except Events.DoesNotExist:
                return Response({"error": "Events not found"}, status=HTTP_404_NOT_FOUND)
            serializer = EventsSerializer(events)
            return Response({"data": serializer.data})
        else:
            events = Events.objects.all().order_by('-created_at')
            serializer = EventsSerializer(events, many=True)
            return Response({"data": serializer.data})

    elif request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            events = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Events not found"}, status=HTTP_404_NOT_FOUND)
        serializer = EventsSerializer(events, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            events = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Events not found"}, status=HTTP_404_NOT_FOUND)
        events.delete()
        return Response({"message": "Events Deleted Successfully"}, status=HTTP_204_NO_CONTENT)




# News API
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def news_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                news = News.objects.get(pk=pk)  
            except News.DoesNotExist:
                return Response({"error": "News not found"}, status=HTTP_404_NOT_FOUND)
            serializer = NewsSerializer(news)
            return Response({"data": serializer.data})
        else:
            news = News.objects.all().order_by('-created_at')
            serializer = NewsSerializer(news, many=True)
            return Response({"data": serializer.data})

    elif request.method == 'POST':
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response({"error": "News not found"}, status=HTTP_404_NOT_FOUND)
        news.delete()
        return Response({"message": "News Deleted Successfully"}, status=HTTP_204_NO_CONTENT)
    #News API End 
    
    # Scheme Api
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def scheme_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                scheme = Scheme.objects.get(pk=pk)
            except Scheme.DoesNotExist:
                return Response({"error": "Scheme not found"}, status=HTTP_404_NOT_FOUND)
            serializer = SchemeSerializer(scheme)
            return Response({"data": serializer.data})
        else:
            scheme = Scheme.objects.all().order_by('-created_at')
            serializer = SchemeSerializer(scheme, many=True)
            return Response({"data": serializer.data})

    elif request.method == 'POST':
        serializer = SchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            scheme = Scheme.objects.get(pk=pk)
        except Scheme.DoesNotExist:
            return Response({"error": "Scheme not found"}, status=HTTP_404_NOT_FOUND)
        serializer = SchemeSerializer(scheme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            scheme = Scheme.objects.get(pk=pk)
        except Scheme.DoesNotExist:
            return Response({"error": "Scheme not found"}, status=HTTP_404_NOT_FOUND)
        scheme.delete()
        return Response({"message": "Scheme deleted successfully"}, status=HTTP_204_NO_CONTENT)
    
    # Scheme API End

# Leads Api Start

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def leads_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                leads = Leads.objects.get(pk=pk)
            except Leads.DoesNotExist:
                return Response({"error": "Leads not found"}, status=HTTP_404_NOT_FOUND)
            serializer = LeadsSerializer(leads)
            return Response({"data": serializer.data})
        else:
            leads = Leads.objects.all().order_by('-created_at')
            serializer = LeadsSerializer(leads, many=True)
            return Response({"data": serializer.data})

    elif request.method == 'POST':
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            leads = Leads.objects.get(pk=pk)
        except Leads.DoesNotExist:
            return Response({"error": "Leads not found"}, status=HTTP_404_NOT_FOUND)
        serializer = LeadsSerializer(leads, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            leads = Leads.objects.get(pk=pk)
        except Leads.DoesNotExist:
            return Response({"error": "Leads not found"}, status=HTTP_404_NOT_FOUND)
        leads.delete()
        return Response({"message": "Leads deleted successfully"}, status=HTTP_204_NO_CONTENT)
    
    # Leads API end
    
    
# Plan API 

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def plan_view(request, pk=None):
#     if request.method == 'GET':
#         if pk:
#             try:
#                 plan = Plan.objects.get(pk=pk)
#                 serializer = PlanSerializer(plan)
#                 return Response({"data": serializer.data})
#             except Plan.DoesNotExist:
#                 return Response({"error": "Plan not found"}, status=HTTP_404_NOT_FOUND)
#         else:
#             plans = Plan.objects.all()
#             serializer = PlanSerializer(plans, many=True)
#             return Response( serializer.data)

#     elif request.method == 'POST':
#         serializer = PlanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( serializer.data, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # elif request.method == 'PUT':
    #     plan = Plan.objects.get(pk=pk)
    #     serializer = PlanSerializer(plan, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         # Check if only the is_active field is being updated
    #         if len(serializer.validated_data) == 1 and 'is_active' in serializer.validated_data:
    #             plan.is_active = serializer.validated_data['is_active']
    #             plan.save()
    #             return Response(serializer.data, status=HTTP_200_OK)
    #         else:
    #             serializer.save()
    #             return Response(serializer.data, status=HTTP_200_OK)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    
   
    
    
    # elif request.method == 'DELETE':
    #     try:
    #         plan = Plan.objects.get(pk=pk)
    #         plan.delete()
    #         return Response({"message": "Plan Deleted Successfully"}, status=HTTP_204_NO_CONTENT)
    #     except Plan.DoesNotExist:
    #         return Response({"error": "Plan not found"}, status=HTTP_404_NOT_FOUND)


def extract_tenure_months(tenure_str):
    """
    Extract the number of months from a tenure string.
    Assumes tenure_str is in the format '<number> Months' or '<number> months'.
    """
    return int(tenure_str.split()[0])

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def plan_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                plan = Plan.objects.get(pk=pk)
                serializer = PlanSerializer(plan)
                return Response(serializer.data)
            except Plan.DoesNotExist:
                return Response({"error": "Plan not found"}, status=HTTP_404_NOT_FOUND)
        else:
            plans = Plan.objects.all()
            # Convert the QuerySet to a list and sort it using the custom key function
            plans = sorted(plans, key=lambda plan: extract_tenure_months(plan.tenure))
            serializer = PlanSerializer(plans, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            plan = Plan.objects.get(pk=pk)
        except Plan.DoesNotExist:
            return Response({"error": "Plan not found"}, status=HTTP_404_NOT_FOUND)

        serializer = PlanSerializer(plan, data=request.data, partial=True)
        if serializer.is_valid():
            # If only is_active field is provided, update just that field
            if len(serializer.validated_data) == 1 and 'is_active' in serializer.validated_data:
                plan.is_active = serializer.validated_data['is_active']
                plan.save()
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    

    elif request.method == 'DELETE':
        try:
            plan = Plan.objects.get(pk=pk)
            plan.delete()
            return Response({"message": "Plan Deleted Successfully"}, status=HTTP_204_NO_CONTENT)
        except Plan.DoesNotExist:
            return Response({"error": "Plan not found"}, status=HTTP_404_NOT_FOUND)





#Subscription API

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def subscription_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                subscription = Subscription.objects.get(pk=pk)
            except Subscription.DoesNotExist:
                return Response({"error": "Subscription not found"}, status=HTTP_404_NOT_FOUND)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        else:
            subscriptions = Subscription.objects.all().order_by('-created_at')
            serializer = SubscriptionSerializer(subscriptions, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            subscription = Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found"}, status=HTTP_404_NOT_FOUND)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            subscription = Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found"}, status=HTTP_404_NOT_FOUND)
        subscription.delete()
        return Response({"message": "Subscription Deleted Successfully"}, status=HTTP_204_NO_CONTENT)
    
    
 
#Apply api
@api_view(['POST'])
def apply_create_view(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)

    data = request.data.copy()  # Make a mutable copy of request.data
    data['company'] = company.id
    serializer = ApplySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data}, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def apply_list_view(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)

    applys = Apply.objects.filter(company=company).order_by('-created_at')
    if not applys.exists():
        return Response({"error": "No applies found for this company"}, status=HTTP_404_NOT_FOUND)
    
    serializer = ApplySerializer(applys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_applied_forms(request):
    user = request.user


    user_applies = Apply.objects.filter(user=user)

    
    if not user_applies.exists():
        return Response({"error": "No applications found for this user"}, status=HTTP_404_NOT_FOUND)

    
    serializer = ApplySerializer(user_applies, many=True)
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_assigned_applications(request):
    # user request
    # import ipdb;
    # ipdb.set_trace()
    user = request.user

    # Get  company associated with user
    try:
        company = Company.objects.get(user=user)
    except Company.DoesNotExist:
        return Response({"message": "User is not associated with any company."}, status=400)

    # Get applications 
    applications = Apply.objects.filter(company=company)
    serialized_data = ApplySerializer(applications, many=True).data
    return Response(serialized_data)






# BUY PLAN

@api_view(['POST'])
def buy_plan(request, plan_id):
    # Token authentication logic here to get the user
    user = request.user

    # Check if the user already has a subscription
    if Subscription.objects.filter(user=user).exists():
        return Response({'message': 'User already buy cannot buy another plan'}, status=HTTP_400_BAD_REQUEST)

    try:
        # Get the plan
        plan = Plan.objects.get(id=plan_id)
    except Plan.DoesNotExist:
        return Response({'error': 'Plan not found'}, status=HTTP_404_NOT_FOUND)
    
    # Create a subscription
    subscription = Subscription.objects.create(user=user, plan=plan)
    
    # Serialize the subscription data
    subscription_serializer = SubscriptionSerializer(subscription)
    
    return Response({'message': 'Plan bought successfully'}, status=HTTP_201_CREATED)

# Get Buy Plan
@api_view(['GET'])
def user_plan(request):
    user = request.user
    if not user.is_authenticated:
        return Response({"error": "User is not authenticated"}, status=HTTP_401_UNAUTHORIZED)
    
    try:
        subscription = Subscription.objects.get(user=user, is_active=True)
        plan = subscription.plan
        plan_details = {
            "name": plan.name,
            "description": plan.description,
            "price": plan.price
            
        }
        return Response({"plan": plan_details}, status=HTTP_200_OK)
    except Subscription.DoesNotExist:
        return Response({"error": "No active plan found for this user"}, status=HTTP_404_NOT_FOUND)
    
    
#ticket raise
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ticket_view(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                ticket = Ticket.objects.get(pk=pk)
                serializer = TicketSerializer(ticket)
                return Response({"data": serializer.data}, status=HTTP_200_OK)
            except Ticket.DoesNotExist:
                return Response({"error": "Ticket not found"}, status=HTTP_404_NOT_FOUND)
        else:
            tickets = Ticket.objects.all().order_by('-created_at')
            serializer = TicketSerializer(tickets, many=True)
            return Response({"data": serializer.data}, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if pk:
            try:
                ticket = Ticket.objects.get(pk=pk)
                serializer = TicketSerializer(ticket, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"data": serializer.data}, status=HTTP_200_OK)
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
            except Ticket.DoesNotExist:
                return Response({"error": "Ticket not found"}, status=HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Method PUT requires a pk"}, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk:
            try:
                ticket = Ticket.objects.get(pk=pk)
                ticket.delete()
                return Response({"message": "Ticket Deleted Successfully"}, status=HTTP_204_NO_CONTENT)
            except Ticket.DoesNotExist:
                return Response({"error": "Ticket not found"}, status=HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Method DELETE requires a pk"}, status=HTTP_400_BAD_REQUEST)