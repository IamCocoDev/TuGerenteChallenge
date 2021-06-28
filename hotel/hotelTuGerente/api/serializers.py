from rest_framework import serializers 
from .models import Client, Booking, BillingData

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields=['id','name', 'last_name', 'email']

class BillingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingData
        fields=['id','name', 'last_name', 'card_number', 'security_code', 'expiration_data']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','status', 'room_details', 'days', "billing_data", 'client', 'amout', 'payment_method']
        depth = 1
        


""" class ClientSerializers(serializers.Serializer):
  name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=30)
  email = serializers.EmailField(max_length=40)

  def create(self, validated_data):
    return ClientSerializers.object.create(validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)

class BillingDataSerializers(serializers.Serializer):
  name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=30)
  card_number = serializers.IntegerField()
  security_code = serializers.IntegerField()
  expiration_data = serializers.IntegerField()

  def create(self, validated_data):
    return BillingDataSerializers.object.create(validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.card_number = validated_data.get('card_number', instance.card_number)
    instance.security_code = validated_data.get('security_code', instance.security_code)
    instance.expiration_data = validated_data.get('expiration_data', instance.expiration_data)

class BookingSerializers(serializers.Serializer):
  status = serializers.CharField(max_length=7)
  room_details = serializers.CharField(max_length=200)
  days = serializers.IntegerField()
  billing_data = serializers.DictField(BillingData)
  client = serializers.DictField(Client)
  amout = serializers.FloatField()
  payment_method = serializers.CharField(max_length=10)

  def create(self, validated_data):
    return BookingSerializers.object.create(validated_data)

  def update(self, instance, validated_data):
    instance.status = validated_data.get('status', instance.status)
    instance.room_details = validated_data.get('room_details', instance.room_details)
    instance.days = validated_data.get('days', instance.days)
    instance.billing_data = validated_data.get('billing_data', instance.billing_data)
    instance.client = validated_data.get('client', instance.client)
    instance.amout = validated_data.get('amout', instance.amout)
    instance.payment_method = validated_data.get('payment_method', instance.payment_method) """