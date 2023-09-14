from django.contrib import admin

from .models import Card, Bid, Product, Photo

# Register your models here.
admin.site.register(Card)
admin.site.register(Bid)
admin.site.register(Product)
admin.site.register(Photo)