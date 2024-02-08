from django.db import models
from users.models import User






class Order:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}: {self.total_price}"


