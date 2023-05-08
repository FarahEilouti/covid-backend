from django.shortcuts import render
from django.http import JsonResponse
from .models import Record
# Create your views here.


def all_countries(request):
    records = Record.objects.all().values()
    return JsonResponse({'records': list(records)})


# def my_records(request):
#     records = Record.objects.all().values()
#     return JsonResponse({'records': list(records)})


def my_records(request):
    if request.method == 'GET':
        records = Record.objects.all().values()
        return JsonResponse({'records': list(records)})
    elif request.method == 'POST':
        # Extract the data from the request
        country = request.POST.get('country')
        date = request.POST.get('date')

        # Create a new record object and save it to the database
        record = Record(country=country, date=date)
        record.save()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return a JSON response indicating failure
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
    
