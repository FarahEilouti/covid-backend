from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Record

def all_countries(request):
    records = Record.objects.all().values()
    return JsonResponse({'records': list(records)})

def my_records(request):
    records = Record.objects.all().values()
    return JsonResponse({'records': list(records)})