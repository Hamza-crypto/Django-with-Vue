from django.db import models

class Order (models.Model):
    card_number = models.CharField(max_length=16)
    pin = models.CharField(max_length=8)

    def __str__(self):
        return self.card_number

