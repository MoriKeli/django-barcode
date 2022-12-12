from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products
from .forms import NewProductForm


def homepage_view(request):
    form = NewProductForm()
    products = Products.objects.all()

    if request.method == 'POST':
        form = NewProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'New product saved successfully!')
            return redirect('homepage')

    context = {'form': form, 'products': products}
    return render(request, 'sales/homepage.html', context)
