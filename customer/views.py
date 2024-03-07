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
        return redirect('customer:login')

    return render(request,'customer/register.html')
def men(request):
    cat=Category.objects.get(name='men')
    pdt=Product.objects.filter(category=cat)
    
    return render(request,'customer/men.html',{'pdt':pdt})
def woman(request):
    cat=Category.objects.get(name='woman')
    pdt=Product.objects.filter(category=cat)
    
    return render(request,'customer/woman.html',{'pdt':pdt})
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
    cart_items=Cart.objects.all()
    total_price=sum(item.product.price*item.quantity for item in cart_items)
    total_price_per_item=[]
    grand_total=0
    for item in cart_items:
        item_total=item.product.price*item.quantity
        total_price_per_item.append({'item':item,'total':'item_total'})
        grand_total+=item_total
    return render(request,'customer/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
def remove_from_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(product=product)
    cart_item.delete()
    return redirect('customer:cart')


def payment(request):
    return render(request,'customer/payment.html')