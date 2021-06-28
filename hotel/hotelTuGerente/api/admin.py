from django.contrib import admin
from .models import Booking, Client, BillingData

# Register your models here.

admin.site.register(Booking)
admin.site.register(Client)
admin.site.register(BillingData)