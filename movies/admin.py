from django.contrib import admin
from hall.models import HallType, Hall, Seat
from movies.models import Genre, AgeLimit, ShowTimes, MovieFormat, Cinema, Movie
from orders.models import Booking, Order
# Register your models here.
admin.site.register(HallType)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Genre)
admin.site.register(AgeLimit)
admin.site.register(ShowTimes)
admin.site.register(MovieFormat)
admin.site.register(Cinema)
admin.site.register(Movie)

