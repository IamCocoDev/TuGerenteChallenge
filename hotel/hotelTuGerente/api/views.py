from typing import ClassVar
from django.core.checks import messages
from django.db.models.fields import AutoField
from django.http import response
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Booking, BillingData
from .serializers import BillingDataSerializer, BookingSerializer, ClientSerializer
from api import serializers

# Aclaracion yo no borro ningun dato, me quedo con todo lo unico que se puede hacer es actualizarlos
# Como una mejora a futuro podria haber agregado un booleano que cuando se mande el id con una peticion http delete se ponga en desactivado=True
# Y que por defecto este en desactivado=False

class BookingViews(APIView):
  # Para traerte todos las reservas o una en especifico con la ruta y el id http://127.0.0.1:8000/booking/?id=1
  def get(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      booking_id= Booking.objects.filter(id=id).first()
      serializer = BookingSerializer(booking_id)
      return Response(serializer.data)
    else:  
      booking = Booking.objects.all() 
      serializer = BookingSerializer(booking, many=True)
      return Response(serializer.data)

  #Para actualizar los datos de una reserva en especifico

  def put(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      booking_id= Booking.objects.filter(id=id).first()
      serializer = BookingSerializer(booking_id,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)
  
  # Para crear una nueva reserva

  def post(self,request,*arg,**kwargs):
    data = request.data
    print(data['billing_data']['name'])
    new_booking = Booking.objects.get_or_create(
      status=data['status'],
      room_details=data['room_details'],
      days=data['days'],
      billing_data=BillingData.objects.get_or_create(
        name=data['billing_data']['name'],
        last_name=data['billing_data']['last_name'],
        card_number=data['billing_data']['card_number'],
        security_code=data['billing_data']['security_code'],
        expiration_data=data['billing_data']['expiration_data']
      )[0],
      client=Client.objects.get_or_create(
        name=data['client']['name'],
        last_name=data['client']['last_name'],
        email=data['client']['email'],
        )[0],
      amout=data['amout'],
      payment_method=data['payment_method']
    )[0]

    new_booking.save()

    serializer = BookingSerializer(new_booking)

    return Response(serializer.data)

class ClientView(APIView):

  # Para traerte todos los usuarios

  def get(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      client= Client.objects.filter(id=id).first()
      serializer = ClientSerializer(client)
      return Response(serializer.data)
    else:  
      client = Client.objects.all()
      serializer = ClientSerializer(client, many=True)
      return Response(serializer.data, status=200)

  # Para crear nuevo usuario

  def post(self,request,*arg,**kwargs):
    data = request.data

    new_client = Client.objects.get_or_create(
      name=data['name'],
      last_name=data['last_name'],
      email=data['email'],
    )[0]

    new_client.save()

    serializer = ClientSerializer(new_client)

    return Response(serializer.data, status=204)

  #Para actualizar los datos de un usuario en especifico

  def put(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      client = Client.objects.filter(id=id).first()
      serializer = ClientSerializer(client,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)



class BillingDataView(APIView):

  # Para todos los datos de facturacion

  def get(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      billindata = BillingData.objects.filter(id=id).first()
      serializer = BillingDataSerializer(billindata)
      return Response(serializer.data)
    else:  
      billindata = BillingData.objects.all() 
      serializer = BillingDataSerializer(billindata, many=True)
      return Response(serializer.data)

  # Para crear nuevos datos de facturacion

  def post(self,request,*arg,**kwargs):
    data = request.data

    new_billing_data = BillingData.objects.get_or_create(
      name=data['name'],
      last_name=data['last_name'],
      card_number=data['card_number'],
      security_code=data['security_code'],
      expiration_data=data['expiration_data'],
    )[0]

    new_billing_data.save()

    serializer = BillingDataSerializer(new_billing_data)

    return Response(serializer.data, status=204)

  #Para actualizar los datos de facturacion de un id en especifico

  def put(self, request):
    if request.query_params:
      id = request.query_params['id']
    else:
      id = 0
    if id != 0:
      billingdata = BillingData.objects.filter(id=id).first()
      serializer = BillingDataSerializer(billingdata,data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)