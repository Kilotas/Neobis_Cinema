from django.contrib import admin
from hall.models import HallType, Hall, Seat
from movies.models import Genre, AgeLimit
# Register your models here.
admin.site.register(HallType)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Genre)
admin.site.register(AgeLimit)
