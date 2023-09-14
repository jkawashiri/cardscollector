from django.db import models

from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    value = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.id})

class Card(models.Model):
    name = models.CharField()
    year = models.IntegerField()
    type = models.CharField()
    value = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    def under_valued(self):
        highest_bid = self.bid_set.order_by('-amount').first()
        if highest_bid:
            return highest_bid.amount > self.value
    
class Bid(models.Model):
    date = models.DateField('purchase date')
    amount = models.IntegerField()

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Placed bid of {self.amount} on {self.date}"
    
    class Meta:
        ordering = ['-amount']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"


    

