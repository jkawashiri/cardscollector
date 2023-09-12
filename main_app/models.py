from django.db import models

from django.urls import reverse

# Create your models here.
class Card(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    type = models.CharField()
    value = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    

