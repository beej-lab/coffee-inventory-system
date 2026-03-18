from django.shortcuts import render, HttpResponse

from inventory.models import Product
from .forms import ProductForm
# Create your views here.


def CreateProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Product created successfully!')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})


def ProductList(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


def ProductDelete(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        return HttpResponse('Product deleted successfully!')
    else:
        return render(request, 'inventory/product_confirm_delete.html', {'product': product})
