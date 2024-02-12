from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PurchaseHistory {self.id}"

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class ClubCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # одному пользователю может быть назначена только одна скидочная карта
    discount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"Club Card for {self.user.username}"

