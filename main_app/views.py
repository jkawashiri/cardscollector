from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card

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

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards'

class CardUpdate(UpdateView):
    model = Card
    fields = ['year', 'type', 'value']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'