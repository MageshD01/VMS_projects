from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Vendor, Product


# ---------------- HOME / DASHBOARD ----------------
@login_required(login_url='login')
def home(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'vendors': users})


# ---------------- SIGNUP ----------------
def signup_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        return redirect('login')
    return render(request, 'signup.html')


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


# ---------------- LOGOUT ----------------
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


# ---------------- VENDOR ----------------
@login_required(login_url='login')
def vendor_form(request):
    if request.method == "POST":
        Vendor.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address')
        )
        return redirect('vendor_list')
    return render(request, 'vendor_form.html')


@login_required(login_url='login')
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})


@login_required(login_url='login')
def vendor_edit(request, id):
    vendor = get_object_or_404(Vendor, id=id)

    if request.method == "POST":
        vendor.name = request.POST.get('name')
        vendor.email = request.POST.get('email')
        vendor.phone = request.POST.get('phone')
        vendor.address = request.POST.get('address')
        vendor.save()
        return redirect('vendor_list')

    return render(request, 'vendor_edit.html', {'vendor': vendor})


@login_required(login_url='login')
def vendor_delete(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()
    return redirect('vendor_list')


# ---------------- PRODUCT ----------------
@login_required(login_url='login')
def product_form(request):
    vendors = Vendor.objects.all()

    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity'),
            vendor_id=request.POST.get('vendor')
        )
        return redirect('product_list')

    return render(request, 'product_form.html', {'vendors': vendors})


@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required(login_url='login')
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    vendors = Vendor.objects.all()

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.vendor_id = request.POST.get('vendor')
        product.save()
        return redirect('product_list')

    return render(request, 'product_edit.html', {'product': product, 'vendors': vendors})


@login_required(login_url='login')
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')
