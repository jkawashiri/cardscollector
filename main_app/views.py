import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card, Product, Photo
from .forms import BidForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class CardList(ListView):
    model = Card
    template_name = 'cards/index.html'

class CardDetail(DetailView):
    model = Card
    template_name = 'cards/detail.html'
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = self.object
        id_list = card.products.all().values_list('id')
        unrelated_products = Product.objects.exclude(id__in=id_list)
        context['bid_form'] = BidForm()
        context['products'] = unrelated_products
        return context

class CardCreate(CreateView):
    model = Card
    fields = ['name', 'year', 'type', 'value']
    success_url = '/cards'

class CardUpdate(UpdateView):
    model = Card
    fields = ['year', 'type', 'value']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'

def add_bid(request, card_id):
    form = BidForm(request.POST)
    if form.is_valid():
        new_bid = form.save(commit=False)
        new_bid.card_id = card_id
        new_bid.save()
    return redirect('detail', pk=card_id)

class ProductList(ListView):
  model = Product

class ProductDetail(DetailView):
  model = Product

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(UpdateView):
  model = Product
  fields = ['name', 'value']

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products'

def assoc_product(request, card_id, product_id):
   Card.objects.get(id=card_id).products.add(product_id)
   return redirect('detail', pk=card_id)

def unassoc_product(request, card_id, product_id):
   Card.objects.get(id=card_id).products.remove(product_id)
   return redirect('detail', pk=card_id)

def add_photo(request, card_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, card_id=card_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', pk=card_id)