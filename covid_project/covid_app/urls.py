from django.urls import path
from . import views

urlpatterns = [
    path('api/all-countries/', views.all_countries, name='all_countries'),
    # Other URL patterns
]