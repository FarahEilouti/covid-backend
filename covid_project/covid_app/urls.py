from django.urls import path
from . import views
from .views import delete_record



urlpatterns = [
    path('api/all-countries/', views.all_countries, name='all_countries'),
    # path('api/add-record/', views.add_record, name='add_record'),
    path('api/delete-record/<int:record_id>/', views.delete_record, name='delete_record'),
    # Other URL patterns
]