from django.db import models

# Creacion de modelos

class Company(models.Model):
    name       = models.CharField(max_length=50)
    website    = models.URLField(max_length=100)
    foundation = models.PositiveBigIntegerField()
