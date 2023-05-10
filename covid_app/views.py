from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
import requests
from .serializers import CovidSerializer
from .models import Covid
        


        
class CovidListView(ListCreateAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer

class CovidDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer


