from django.db import models
from users.models import User
from movies.models import ShowTimes
from hall.models import Seat
from users.models import ClubCard

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.user}: {self.total_price}"

    class Meta:
        verbose_name = "Заказ"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTimes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.seat} - {self.showtime}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Бронь"

class TicketCategory(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.price}"

    class Meta:
        verbose_name = "Тип билета"

class Ticket(models.Model):
    price = models.IntegerField(blank=True, null=True, default=0)
    ticket_type = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTimes, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price = (self.ticket_type.price + self.showtime.hall.hall_type.price +
                 self.showtime.movie.movie_format.price)

        club_card = ClubCard.objects.filter(user=self.user).first()

        discount = club_card.discount if club_card else 0

        if discount > 0:
            price_with_discount = price * (100 - discount) / 100
            self.price = round(price_with_discount, 2)
        else:
            self.price = price

        super().save(*args, **kwargs)

