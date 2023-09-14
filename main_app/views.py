from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
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
        context['bid_form'] = BidForm()
        return context

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

def add_bid(request, card_id):
    form = BidForm(request.POST)
    if form.is_valid():
        new_bid = form.save(commit=False)
        new_bid.card_id = card_id
        new_bid.save()
    return redirect('detail', pk=card_id)