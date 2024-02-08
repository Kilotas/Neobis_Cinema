from django.db import models

# Create your models here.

# Create your models here.
class HallType(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return f" The id {self.id}: the name {self.name} - the price {self.price}"

class Hall(models.Model):
    name = models.CharField(max_length=20)
    hall_type = models.ForeignKey(HallType, on_delete=models.CASCADE)

class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seat = models.PositiveIntegerField()

    def __str__(self):
        return f"The id is {self.id}: the hall {self.hall} - the seats {self.seat}"

