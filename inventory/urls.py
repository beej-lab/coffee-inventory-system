from django.urls import path
from . import views

urlpatterns = [
    path('createproduct/', views.CreateProduct, name='create-product'),
    path('productlist/', views.ProductList, name='product-list'),
    path('deleteproduct/<int:pk>/', views.ProductDelete, name='delete-product'),
]
