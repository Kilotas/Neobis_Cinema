from django.contrib import admin
from .models import Order, Booking, TicketCategory, Ticket
# Register your models here.

admin.site.register(Order)
admin.site.register(Booking)
admin.site.register(TicketCategory)
admin.site.register(Ticket)

