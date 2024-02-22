from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('men/',views.men,name='men'),
    path('woman/',views.woman,name='woman'),
    path('masterpage/',views.masterpage,name='masterpage'),
    path('cart/',views.cart,name='cart'),
    path('payment/',views.payment,name='payment')
]
