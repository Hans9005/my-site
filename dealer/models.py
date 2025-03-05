from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()  # пробіг в км
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True)


    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"





class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale of {self.car} to {self.customer} on {self.sale_date}"
