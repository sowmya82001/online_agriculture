from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Crop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, default="Unknown")  # Add default value
    quantity = models.IntegerField(default=0)  # Add default value



    def __str__(self):
        return self.name

class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.crop.name} ({self.quantity})"
