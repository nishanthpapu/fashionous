from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
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
        # if Seller.objects.filter(email=email,password=password).exists():
        #     return redirect('seller:s_home')
        # else:
        try:
            sell=Seller.objects.get(email=email,password=password)
            request.session['seller']=sell.id
            return redirect('seller:s_home')
        except Seller.DoesNotExist:
            return render(request,'seller/s_login.html ',{'msg':'invalid password'})
    return render(request,'seller/s_login.html')
def s_logout(request):
    if 'seller' in request.session:
        del request.session['seller']
        return redirect('seller:s_login')
def add_product(request):
    if 'seller' in request.session:
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
            messages.success(request,'Product added successfully!')
        return render(request,'seller/add_product.html',{'cat':cat})
    else:
        return render(request,'seller/s_home.html')
    
def view_product(request):
    if 'seller' in request.session:
        pdt=Product.objects.all()
        return render(request,'seller/view_product.html',{'pdt':pdt})
    else:
        return render(request,'seller/s_home.html')   
    
def update_product(request,pid):
    if 'seller' in request.session:
        cat=Category.objects.all()
        product=Product.objects.get(id=pid)
        if request.method=='POST':
            name=request.POST['name']
            description=request.POST['description']
            quantity=request.POST['quantity']
            price=request.POST['price']
            image=request.FILES['image']
            product.name=name
            product.description=description
            product.quantity=quantity
            product.price=price
            product.image=image
            product.save()
            messages.success(request,'Product updated successfully!')
            return redirect('seller:view_product')
        return render(request,'seller/update_product.html',{'product':product,'cat':cat})
    else:
        return render(request,'seller/s_home.html')  

    
def remove(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('seller:view_product')