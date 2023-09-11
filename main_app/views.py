from django.shortcuts import render

cards = [
    {'name': 'Lebron James', 'year': 2003, 'type': 'Topps Chrome'},
    {'name': 'Shohei Ohtani', 'year': 2018, 'type': 'Bowman Chrome Autograph'},
    {'name': 'Tiger Woods', 'year': 2001, 'type': 'SP Authentic Autograph'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    return render(request, 'cards/index.html', {
        'cards': cards
    })