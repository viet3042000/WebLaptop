import json

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import get_current_timezone

from Account.forms import Profile
from Checkout.models import Order, Order_Product
from Shop.views import Same, Product
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.
def checkout(request):
    (cart, cart_product) = Same(request)
    customer = request.user.customer
    profile = Profile()

    if request.method == "POST":
        form = Profile(request.POST)
        if form.is_valid():
            name = request.POST['full_name']
            address = request.POST['address']
            email = request.POST['email']
            phone = request.POST['phone']
            description = request.POST['ordernode']
            if len(cart_product) != 0:
                order = Order.objects.filter(customer=customer)
                print(order)
                if len(order) != 0:
                    if order[len(order) - 1].status != "New":
                        order = Order.objects.create(customer=customer, name=name, address=address, email=email,
                                                     phone=phone, description=description)
                        order.save()
                    else:
                        order, create = Order.objects.get_or_create(customer=customer, name=name, address=address,
                                                                    status="New",
                                                                    email=email, phone=phone, description=description)
                        order.save()
                else:
                    order, create = Order.objects.get_or_create(customer=customer, name=name, address=address,
                                                                email=email, phone=phone, description=description)
                    order.save()
                for p in cart_product:
                    order_product = Order_Product.objects.create(order=order, product=p.product, quantity=p.quantity)
                    order_product.save()
                cart_product.delete()
                cart.delete()
                messages.success(request, "Đặt hàng thành công!")
            else:
                messages.warning(request, "Thêm vào giỏ hàng!")
        else:
            messages.warning(request, "Thông tin chưa hợp lệ!")
    context = {
        'cart': cart,
        'cart_product': cart_product,
        'customer': customer,
        'profile': profile,
    }
    return render(request, 'testCheckOut.html', context)


@login_required(login_url='login')
def orderdetail(request, id):
    (cart, cart_product) = Same(request)
    order = Order.objects.get(id=id)
    if order.status == "onShipping":
        order = Order.objects.get(pk=id)
        order.date_ship = datetime.now(tz=get_current_timezone())
        order.save()

    order_product = Order_Product.objects.filter(order=order)

    if order.status == "Completed":
        for order_product1 in order_product:
            order_product1.product.quantity = order_product1.product.quantity - order_product1.quantity
            order_product1.product.quantitySelled = order_product1.product.quantitySelled + order_product1.quantity
            order_product1.product.save()
    context = {
        'cart': cart,
        'cart_product': cart_product,
        'order_product': order_product,
        'order': order,
    }
    return render(request, 'orderdetail.html', context)


def update_order(request):
    data = json.loads(request.body)
    Id = data['Id']
    action = data['action']

    order = Order.objects.get(pk=Id)
    if action == "cancel":
        order.status = "Canceled"
        order.save()
    else:
        order.status = "Success"
        order.date_finnish = datetime.now(tz=get_current_timezone())
        order.save()
    return JsonResponse("order is updated", safe=False)
