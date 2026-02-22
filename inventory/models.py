from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    name = models.CharField(max_length=100)  # Name of ingredient
    category = models.CharField(max_length=50)  # Type of ingredient
    unit = models.CharField(max_length=20)  # Current quantity of ingredient
    minimum_threshold = models.FloatField(default=0)    # Low stock alert
    # States the current date and time
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('RESTOCK', 'Restock'),
        ('DEDUCT', 'Deduct'),
        ('SPOILED', 'Spoiled')
    ]

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_TYPES)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.movement_type} - {self.quantity} {self.unit} of {self.ingredient.name}"
