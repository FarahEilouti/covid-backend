from django.urls import path
from . import views
from .views import add_record


urlpatterns = [
    path('api/all-countries/', views.all_countries, name='all_countries'),
    path('api/add-record/', views.add_record, name='add_record'),
    # Other URL patterns
]