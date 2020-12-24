import json

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Account.models import Customer
from Shop.models import *
from .filter import *
from .models import Admin
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def adminhome(request):
    if Admin.objects.filter(user=request.user).exists():

        return render(request, 'Admin/adminhome.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def adminbrands(request):
    if Admin.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            brand = Brand()
            brand.brandName = request.POST.get('brand_title')
            brand.description = request.POST.get('brand_desc')
            brand.save()
            messages.success(request, 'Them brand thanh cong')
        return render(request, 'Admin/brands.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def admincategory(request):
    if Admin.objects.filter(user=request.user).exists():
        if request.method == 'POST':
            category = Category()
            category.categoryName = request.POST.get('cat_title')
            category.description = request.POST.get('category_desc')
            category.save()
            messages.success(request, 'Them category thanh cong')
        return render(request, 'Admin/category.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def adminproducts(request):
    if Admin.objects.filter(user=request.user).exists():
        products = Product.objects.all()
        context = {
            'products': products,
        }
        return render(request, 'Admin/products.html', context)
    else:
        return redirect('login')


@login_required(login_url='login')
def adminorders(request):
    if Admin.objects.filter(user=request.user).exists():
        return render(request, 'Admin/orders.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def admincustomers(request):
    if Admin.objects.filter(user=request.user).exists():

        customers = Customer.objects.all()
        myfilter = customerFilter(request.GET, queryset=customers)
        customers = myfilter.qs
        print(customers)
        context = {
            'customers': customers,
            'myfilter': myfilter,
        }
        return render(request, 'Admin/customers.html', context)
    else:
        return redirect('login')


@login_required(login_url='login')
def admindashboard(request):
    if Admin.objects.filter(user=request.user).exists():
        return render(request, 'Admin/dashboard.html')
    else:
        return redirect('login')


@login_required(login_url='login')
def updateUser(request):
    data = json.loads(request.body)
    id = data['id']
    action = data['action']
    print("id:", id, "action :", action)
    customer = Customer.objects.get(id=id)
    customer.delete()
    return JsonResponse('update success', safe=False)


@login_required(login_url='login')
def updateProduct(request):
    return JsonResponse('update success', safe=False)
