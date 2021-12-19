from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    # request.session['total_items'] = 0
    # request.session['total_spent'] = 0    
    context = {
        "all_products": Product.objects.all(),
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST["product_id"])
    price_from_form = float(product.price)
    total_charge = quantity_from_form * price_from_form
    # total_charge = round(total_charge,2)          WHY DOESN'T THIS WORK?
    total_spent = request.session['total_spent']
    # total_spent = round(total_spent,2)            WHY DOESN'T THIS WORK?
    request.session['total_charge'] = total_charge 
    request.session['total_items'] += quantity_from_form
    request.session['total_spent'] += total_charge
    print("Charging credit card in checkout...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/display_checkout_page/")

def display_checkout_page(request):
    total_spent = request.session['total_spent']

    context = {
        "total_charge" : request.session['total_charge'],
        "total_items" : request.session['total_items'],
        "total_spent" : "{:.2f}".format(total_spent),
    }
    print("Charging credit card in display_checkout_page...")
    return render(request,"store/checkout.html",context)