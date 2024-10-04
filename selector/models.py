from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=150)

class Model(models.Model):
    name = models.CharField(max_length=50)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

class CarType(models.Model):
    name = models.CharField(max_length=50)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
