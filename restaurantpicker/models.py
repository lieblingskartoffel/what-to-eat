from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeliveryApp(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    cuisine_id = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    app_id = models.ForeignKey(DeliveryApp, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
