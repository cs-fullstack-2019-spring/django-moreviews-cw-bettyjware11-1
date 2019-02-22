from django.db import models


# Create your models here.
# name, material, and manufacturerDate
class Cup(models.Model):
    name = models.CharField(max_length=200, default="")
    material = models.CharField(max_length=200, default="")
    manufactuerDate = models.DateField(default="")




# phoneApp
# from django.db import models
#
# # Create your models here.
# class Phone(models.Model):
#     name = models.CharField(max_length=200, default="")
#     hoursOfBattery = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
#     version = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.name

# computerApp
# from django.db import models
#
# # Create your models here.
# class Computer(models.Model):
#     name = models.CharField(max_length=200, default="")
#     cores = models.IntegerField(default=0)
#     speed = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
#
#     def __str__(self):
#         return self.name
