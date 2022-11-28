from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from .serializers import wasteSerializer
from .models import wastes
import HouseOwnerApp.models as ho_models
import HouseOwnerApp.serializers as ho_serializers


@api_view(['GET'])
def getWastes(request):
    wasteList = wastes.objects.all()
    serializer = wasteSerializer(wasteList, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postCorporationlogin(request):
    data_username = request.data['username']
    data_password = request.data['password']

    # user = houseowner.objects.filter(email = data_email).first()

    if data_username!="admin":
        raise AuthenticationFailed('User not found')
    if data_password!="admin":
        raise AuthenticationFailed('Incorrect password')
    payload = {
        'id':"admin",
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret',algorithm='HS256')
    response =  Response()
    response.set_cookie(key = 'jwt',value=token, httponly=True)
    response.data = {'jwt': token}
    return response

@api_view(['POST'])
def postBookingReport(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError :
        raise AuthenticationFailed('Unauthenticated!')
    
    ward_no = request.data['ward_no']
    # collection_date = request.data['collection_date']

    users = ho_models.houseowner.objects.filter(wardno = ward_no)
    # ho_serializer = ho_serializers.houseOwnerSerializer(users,many = True)
    for ho in users:
        slots = ho_models.slotbooking.objects.filter(houseowner_id = ho.id)
        slots_serializer = ho_serializers.slotBookingSerializer(slots,many = True)
        # data = slots_serializer.data[:]
    return Response(slots_serializer.data)
