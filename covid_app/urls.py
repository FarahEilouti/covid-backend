from django.urls import path
from .views import CovidListView,CovidDetailView
urlpatterns=[

    
    path('',CovidListView.as_view()),
    path('<pk>',CovidDetailView.as_view()),

#api/v1/covid/
]