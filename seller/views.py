from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def s_home(request):
    return render(request,'seller/s_home.html')
def s_register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        email=request.POST['email']
        sell=Seller(firstname=firstname,lastname=lastname,password=password,email=email)
        sell.save()
        return redirect('seller:s_login')
    return render(request,'seller/s_register.html')
def s_login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Seller.objects.filter(email=email,password=password).exists():
            return redirect('seller:s_home')
        else:
            return render(request,'seller/s_login',{'msg':'invalid password'})

    return render(request,'seller/s_login.html')
def add_product(request):
    cat=Category.objects.all()
    if request.method=='POST':
        Name=request.POST['name']
        Description=request.POST['description']
        Quantity=request.POST['quantity']
        Price=request.POST['price']
        Image=request.FILES['image']

        category_id=request.POST.get('cat')
        category=Category.objects.get(id=category_id)
        Pdt=Product(name=Name,description=Description,quantity=Quantity,price= Price,image=Image,category=category)
        Pdt.save()
    return render(request,'seller/add_product.html',{'cat':cat})
def view_product(request):
    pdt=Product.objects.all()
    return render(request,'seller/view_product.html',{'pdt':pdt})
def update_product(request,pid):
    cat=Category.objects.all()
    product=Product.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        quantity=request.POST=['quantity']
        price=request.POST['price']
        image=request.FILES['image']
        product.name=name
        product.description=description
        product.quantity=quantity
        product.price=price
        product.image=image
        product.save()
        return redirect('seller:view_product')

    return render(request,'seller/update_product.html',{'product':product,'cat':cat})
def remove(request,category_id):
    Product.objects.get(id=category_id).delete()
    return redirect('seller:view_product')