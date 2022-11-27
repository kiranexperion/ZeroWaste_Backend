from .import views
from django.urls import path

urlpatterns = [
    path('wastelist/',views.getWastes,name = 'wastes'),
]