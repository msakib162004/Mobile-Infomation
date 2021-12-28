from django.db import models


class MobileInformation(models.Model):
    Brand_Name = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    JAN_Code = models.CharField(max_length=200, unique=True)
    Image = models.TextField()
