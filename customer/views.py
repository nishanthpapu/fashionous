from django.shortcuts import render, redirect
from customer.models import *

# Create your views here.
def home(request):
    return render(request,'customer/home.html')
def about(request):
    return render(request,'customer/about.html')
def contact(request):
    return render(request,'customer/contact.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psd']
        if Customer.objects.filter(email=email,password=password).exists():
            return redirect('customer:home')
        else:
            return render(request,'customer/login.html',{'msg':'invalid password'})
    return render(request,'customer/login.html')
def register(request): 
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        email=request.POST['email']
        cust=Customer(firstname=firstname,lastname=lastname,password=password,email=email)
        cust.save()
        return redirect('customer:login')

    return render(request,'customer/register.html')
def men(request):
    return render(request,'customer/men.html')
def woman(request):
    return render(request,'customer/woman.html')
def masterpage(request):
    return render(request,'customer/masterpage.html')
def cart(request):
    return render(request,'customer/cart.html')
def payment(request):
    return render(request,'customer/payment.html')