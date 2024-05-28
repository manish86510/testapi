
from rest_framework.decorators import api_view
from rest_framework.response import Response
from companyprofile.models import Company,Service
from .serializers import ServiceSerializer,CompanySerializer,IndustrySerializer,EventsSerializer, NewsSerializer, SchemeSerializer ,LeadsSerializer 
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers
from .models import *
from Auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
# from rest_framework import viewsets

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

# Create your views here.
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'name', 'date_of_birth', 'email', 'is_active', 'date_joined']

class GetUserFromToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_data = request.user
        serializer = CustomUserSerializer(user_data)
        return Response({'data': serializer.data})


@api_view(['POST'])
def add_service(request):
    if request.method == 'POST': 
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

    
@api_view(['GET'])
def get_all_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_company(request):
    if request.method == 'POST':
        email = request.user.email
        user = User.objects.get(email=email)
        company_data = request.data
        company_data['created_by'] = user.pk  # Store user's ID as created_by
        serializer = CompanySerializer(data=company_data)
        if serializer.is_valid():
            serializer.save(created_by=user)  # Set the created_by field in the serializer
            return Response({"data": serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    
@api_view(['GET'])
def get_all_company(request):
    company= Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_company(request, pk):
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return Response({"error": "Company not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def get_all_industry(request):
    industry = Industry.objects.all()
    serializer= IndustrySerializer(industry, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def add_industry(request):
    if request.method == 'POST':
        serializer = IndustrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['PUT'])
def update_industry(request, pk):
    try:
        industry = Industry.objects.get(pk=pk)
    except Industry.DoesNotExist:
        return Response({"error": "Industry not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = IndustrySerializer(industry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_industry(request, pk):
    try:
        industry = Industry.objects.get(pk=pk)
    except Industry.DoesNotExist:
        return Response({"error": "Industry not found"}, status=HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        industry.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
    
    
    
# EVENTS GET API
@api_view(['GET'])
def get_all_events(request):
    events = Events.objects.all()
    serializer=EventsSerializer(events, many=True)
    return Response({"data":serializer.data})

# EVENTS ADD API
@api_view(['POST'])
def add_events(request):
    if request.method =='POST':
        serializer=EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)       
    
    
#EVENTS UPDATE API



#EVENTS DELETE API


#NEWS GET API
@api_view(['GET'])
def get_all_news(request):
    news=News.objects.all()
    serializers=NewsSerializer(news, many=True)
    return Response({"data":serializers.data}) 

#NEWS ADD API
def add_news(request):
    if request.method=='POST':
        serializer=NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.data,status=HTTP_400_BAD_REQUEST)
           
           
#NEWS  UPDATE API


#NEWS DELETE API


#SCHEME GET API
@api_view(['GET'])
def get_all_scheme(request):
    scheme=Scheme.objects.all()
    serializers=NewsSerializer(scheme, many=True)
    return Response({"data":serializers.data}) 
    
    
#SCHEME ADD API
def add_scheme(request):
    if(request.method=='POST'):
        serializer=SchemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.data,status=HTTP_400_BAD_REQUEST)

#SCHEME UPDATE API


#SCHEME DELETE API



#LEADS GET API
@api_view(['GET'])
def get_all_leads(request):
    leads=Leads.objects.all()
    serializers=LeadsSerializer(leads, many=True)
    return Response({"data":serializers.data}) 

#LEADS ADD API
def add_leads(request):
    if request.method=='POST':
        serializer=LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.data,status=HTTP_400_BAD_REQUEST)