from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Client(models.Model):
  id=models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=40)

  def __str__(self):
      return self.name + ' ' +self.last_name

class BillingData(models.Model):
  id=models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  card_number = models.CharField(max_length=19)
  security_code = models.IntegerField()
  expiration_data = models.IntegerField()

  def __str__(self):
      return self.name + ' ' +self.last_name


class Booking(models.Model):
  id=models.AutoField(primary_key=True)
  status = models.CharField(max_length=7)
  room_details = models.CharField(max_length=200)
  days = models.IntegerField()
  billing_data = models.ForeignKey(BillingData, on_delete=CASCADE)
  client = models.ForeignKey(Client, on_delete=CASCADE)
  amout = models.FloatField()
  payment_method = models.CharField(max_length=20)

  def __str__(self):
      return self.status