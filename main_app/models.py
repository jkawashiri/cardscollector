from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    type = models.CharField()
    value = models.IntegerField()

    def __str__(self):
        return self.name
    

