from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import houseOwnerSerializer
from .serializers import wardsSerializer
from .models import houseowner
from .models import wards

import jwt, datetime


@api_view(['POST'])
def postHouseOwner(request):
    serializer = houseOwnerSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response({'status':1,'message':'Successfully Saved','data':serializer.data})
    else:
        return Response({'status':0,'message':'OOPS Some error occured','data':serializer.errors})

@api_view(['GET'])
def getWards(request):
    wardsList = wards.objects.all()
    serializer = wardsSerializer(wardsList, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postHouseOwnerlogin(request):
    data_email = request.data['email']
    data_password = request.data['password']

    user = houseowner.objects.filter(email = data_email).first()

    if user is None:
        raise AuthenticationFailed('User not found')
    if not user.check_password(data_password):
        raise AuthenticationFailed('Incorrect password')
    payload = {
        'id':user.id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret',algorithm='HS256')
    response =  Response()
    response.set_cookie(key = 'jwt',value=token, httponly=True)
    response.data = {'jwt': token}
    return response

@api_view(['POST'])
def postLogoutView(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {'message': 'success','status':1}
    return response

@api_view(['GET'])
def getUserView(request):
    token = request.COOKIES.get('jwt')
    print("token:",token)
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError :
        raise AuthenticationFailed('Unauthenticated!')

    user = houseowner.objects.filter(id = payload['id'])
    serializer = houseOwnerSerializer(user,many=True)
    return Response(serializer.data)