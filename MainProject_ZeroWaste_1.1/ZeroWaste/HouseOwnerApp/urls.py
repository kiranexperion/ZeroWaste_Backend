from .import views
from django.urls import path

urlpatterns = [

    path('houseowner/signup/',views.postHouseOwner,name = 'signup'),
    # path('houseowner/signup/get',views.getHouseOwner,name = 'signup'),
    path('houseowner/login/',views.postHouseOwnerlogin,name = 'login'),
    path('houseowner/logout/',views.postLogoutView),
    path('wards/',views.getWards,name='wards'),
    path('user/',views.getUserView),

]