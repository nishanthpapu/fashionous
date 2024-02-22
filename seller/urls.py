from django.urls import path
from.import views
app_name='seller'
urlpatterns =[
    path('s_home/',views.s_home,name='s_home'),
    path('s_register/',views.s_register,name='s_register'),
    path('s_login/',views.s_login,name='s_login'),
    path('add_product/',views.add_product,name='add_product'),
    path('view_product/',views.view_product,name='view_product'),
    path('update_product/',views.update_product,name='update_product'),
    path('remove/<int:pid>',views.remove,name='remove'),
    path('update/<int:pid>',views.update_product,name='update_product')
]