from .import views
from django.urls import path

urlpatterns = [
    path('wastelist/',views.getWastes,name = 'wastes'),
    path('corporation/login',views.postCorporationlogin,name='login'),
    path('corporation/bookingreport',views.postBookingReport,name='bookingreport'),

]