from django.http import request
from django.shortcuts import render
from django.utils.translation import to_locale
from .models import Product, Location, ProductMovement
from django.contrib import messages
from .forms import ProductForm, LocationForm
from django.shortcuts import get_object_or_404, HttpResponseRedirect


def Manage(request):
    return render(request, 'home.html')


def add_product(request):
    if request.method == 'POST':
        if request.POST.get('Product_id') and request.POST.get('Quantity'):
            post = Product()
            post.Product_id = request.POST.get('Product_id')
            post.Quantity = request.POST.get('Quantity')
            post.reserved_quantity = request.POST.get("Quantity")
            post.save()
            messages.success(request, "Product Added Sucessfully")
            return render(request, 'add_product.html')

    else:
        return render(request, 'add_product.html')


def edit_product(request, Product_id):
    context = {}

    obj = get_object_or_404(Product, Product_id=Product_id)

    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/view_product")

    context["form"] = form

    return render(request, "edit_product.html", context)


def view_product(request):
    items_list = Product.objects.all()
    context = {
        'items_list': items_list,
    }
    return render(request, 'view_product.html', context)


def add_location(request):
    if request.method == 'POST':
        if request.POST.get('Location_id') and request.POST.get('Address') and request.POST.get('Product') and request.POST.get('Quantity'):
            post = Location()
            product = request.POST.get('Product')
            if not product:
                messages.error("Product not found")
                return render(request, "add_location.html")
            product_obj = Product.objects.filter(id=product).first()
            if not product_obj:
                messages.error('Product not found')
                return render(request, "add_location.html")

            post.Location_id = request.POST.get('Location_id')
            post.Address = request.POST.get('Address')
            post.Product = request.POST.get('Product')
            post.quantity = request.POST.get('Quantity')
            post.save()
            messages.success(request, "Location Added Sucessfully")
            return render(request, 'add_location.html')

    else:
        messages.error("enter value")
        return render(request, 'add_location.html')


def edit_location(request, Location_id):
    context = {}

    obj = get_object_or_404(Location, Location_id=Location_id)

    form = LocationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/view_location")

    context["form"] = form

    return render(request, "edit_location.html", context)


def view_location(request):
    items_list = Location.objects.all()
    context = {
        'items_list': items_list,
    }
    return render(request, 'view_location.html', context)


def productMovement(request, Product_id):
    from_location = Location.objects.get(Address=request.POST.get("from"))
    product = Product.objects.get(pk=Product_id)
    quantity = request.POST.get("quantity")
    to_location = Location.objects.get(Address=request.POST.get('to'))
    if to_location.Product != product:
        messages.error("product not found")
    if from_location.Quantity > int(quantity):
        Product.quantity = Product.quantity-int(quantity)
        Product.save()
        transaction = ProductMovement(
            Quantity=quantity, Product_id=product, from_location=from_location, to_location=to_location)
        transaction.save()

    return render(request, 'move_product.html')
