from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.CardList.as_view(), name='index'),
    path('cards/<int:pk>/', views.CardDetail.as_view(), name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_bid/', views.add_bid, name='add_bid'),
    path('products/', views.ProductList.as_view(), name='products_index'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('products/create/', views.ProductCreate.as_view(), name='products_create'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),
]