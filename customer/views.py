from django.shortcuts import render, redirect
from customer.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def home(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        customer=cust.firstname
        customer=customer[0]
    return render(request,'customer/home.html')
def about(request):
    return render(request,'customer/about.html')
def mobile(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['contact']
        text=request.POST['text']
        mob=Customer(name=name,email=email,contact=contact,text=text)
        mob.save()
    return render(request,'customer/mobile.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['psd']
        try:
            cust=Customer.objects.get(email=email,password=password)
            request.session['customer']=cust.id
            return redirect('customer:home')
        except Customer.DoesNotExist:
            return render(request,'customer/login.html',{'msg':'invalid password'})
    return render(request,'customer/login.html')
    
def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return redirect('customer:login')
def register(request): 
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        email=request.POST['email']
      
        cust=Customer(firstname=firstname,lastname=lastname,password=password,email=email)
        
        cust.save()
        messages.success(request,'Registered Successfully!')
        
        return render(request,'customer/register.html')
        
    return render(request,'customer/register.html')
        
    
def men(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cat=Category.objects.get(name='men')
        pdt=Product.objects.filter(category=cat)
        cust=Customer.objects.get(id=customer_id)
        customer=cust.firstname
        customer=customer[0]
    
    return render(request,'customer/men.html',{'pdt':pdt,'cust':customer})
def woman(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        cat=Category.objects.get(name='woman')
        pdt=Product.objects.filter(category=cat)
        customer=cust.firstname
        customer=customer[0]
    
        return render(request,'customer/woman.html',{'pdt':pdt,'customer':cust,'cust':customer})
    else:
        return redirect('customer:home')
def masterpage(request):
    return render(request,'customer/masterpage.html')
def add_to_cart(request,product_id):
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
    return redirect('customer:cart')

def cart(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)
        cart_items=Cart.objects.all()
        total_price=sum(item.product.price*item.quantity for item in cart_items)
        total_price_per_item=[]
        grand_total=0
    for i in cart_items:
        tot=i.product.price * i.quantity
    for item in cart_items:
        item_total=item.product.price*item.quantity
        total_price_per_item.append({'item':item,'total':'item_total'})
        grand_total+=item_total
    customer=cust.firstname
    customer=customer[0]
    return render(request,'customer/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price,'item_total':item_total,'tot':tot,'cust':customer})
def remove_from_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(product=product)
    cart_item.delete()
    return redirect('customer:cart')


def payment(request):
    return render(request,'customer/payment.html')
def myaccount(request):
    if 'customer' in request.session:
        customer_id=request.session.get('customer')
        cust=Customer.objects.get(id=customer_id)

    return render(request,'customer/myaccount.html',{'customer':cust})