import json
import datetime

from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import *
from .filter import *


# Create your views here.
def Home(request):
    newProduct = Product.objects.order_by('dateAdded')[0:6]
    topSelling = Product.objects.order_by('-quantitySelled')[0:6]
    (cart, cart_product) = Same(request)
    context = {
        'newProduct': newProduct,
        'topSelling': topSelling,
        'cart': cart,
        'cart_product': cart_product,
    }
    return render(request, 'Shop/Home.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    quantity = data['quantity']
    print("quantity", quantity)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_product, created = Cart_Product.objects.get_or_create(cart=cart, product=product)
    if action == 'add' and product.quantity >= int(quantity):
        cart_product.quantity = (cart_product.quantity + int(quantity))
        if cart_product.quantity > product.quantity:
            cart_product.quantity = product.quantity
        cart_product.save()

    elif action == 'remove':
        cart_product.delete()

    return JsonResponse("cart is updated", safe=False)


def Same(request):
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        cart, created = Cart.objects.get_or_create(customer=customer)
        cart_product = cart.cart_product_set.all()

    else:
        cart_product = []
        cart = {'get_total_product': 0, 'get_total_price_product': 0}

    return (cart, cart_product)


def Store(request):
    Allproducts = Product.objects.all()

    myfilter = productFilter(request.GET, queryset=Allproducts)
    Allproducts = myfilter.qs

    search = request.POST.get('myInput')
    if request.method == "POST" and search is not None:
        Allproducts = Product.objects.filter(name__icontains=search)

    if request.method == 'GET' and request.is_ajax():
        data = {}
        myfilter = productFilter(request.GET, queryset=Allproducts.values())
        Allproduct = list(myfilter.qs)
        data['products'] = json.dumps(Allproduct, default=myconverter)
        return JsonResponse(data, status=200)

    paginator = Paginator(Allproducts, 8)
    pagenum = request.GET.get('page', 1)
    numPage = paginator.num_pages  ### get number of page
    (cart, cart_product) = Same(request)

    try:
        products = paginator.page(pagenum)
    except (EmptyPage, InvalidPage, ValueError):
        products = paginator.page(1)
    context = {
        'products': products,
        'numPage': range(1, numPage + 1),
        'cart': cart,
        'cart_product': cart_product,
        'myfilter': myfilter,
        'search': search,
    }
    return render(request, 'Shop/Store.html', context)


def myconverter(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()


def product(request, id):
    productid = get_object_or_404(Product, pk=id)
    productRelate = Product.objects.filter(brand=productid.brand)[0:4]
    (cart, cart_product) = Same(request)
    images = Images.objects.filter(product_id=id)
    context = {
        'product': productid,
        'productRelate': productRelate,
        'images': images,
        'cart': cart,
        'cart_product': cart_product,
    }
    return render(request, 'Shop/product.html', context)


def aboutUs(request):
    (cart, cart_product) = Same(request)
    return render(request, 'Shop/aboutUS.html', {'cart': cart, 'cart_product': cart_product})


# def contact(request):
#     return render(request, 'Shop/contact.html')

def contact(request):
    (cart, cart_product) = Same(request)
    if request.method == 'POST':
        subject = 'Subject here',
        message = 'Here is the message.',
        email_from = settings.EMAIL_HOST_USER,
        recipient_list = [request.POST.get('email_receive')],
        email_template_name = "Shop/mailContact.txt",
        email = render_to_string(email_template_name)
        send_mail(
            'Thông tin khuyến mãi',
            email,
            settings.EMAIL_HOST_USER,
            recipient_list[0],
        )
        messages.success(request, "Email của bạn đã được gửi thông tin"),
    else:
        messages.warning(request, "Mời nhập email")
    return render(request, 'Shop/contact.html', {'cart': cart, 'cart_product': cart_product})


def privacypolicy(request):
    (cart, cart_product) = Same(request)
    return render(request, 'Shop/privacypolicy.html', {'cart': cart, 'cart_product': cart_product})


def ordersandreturns(request):
    (cart, cart_product) = Same(request)
    return render(request, 'Shop/ordersandreturns.html', {'cart': cart, 'cart_product': cart_product})


def termandconditions(request):
    (cart, cart_product) = Same(request)
    return render(request, 'Shop/termsandconditions.html', {'cart': cart, 'cart_product': cart_product})


def help(request):
    (cart, cart_product) = Same(request)
    return render(request, 'Shop/help.html', {'cart': cart, 'cart_product': cart_product})
