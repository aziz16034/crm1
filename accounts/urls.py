from django.urls import path, include
from .views import *
from .models import *
from django.conf.urls import url



urlpatterns = [
    url(r'^$', loginPage, name='loginPage'),
    url(r'^home/$', home, name='home'),

    url('contact_us/', contact_us, name='contact_us'),
    url('about/', about),
    url('product_item/', product_item, name = 'product_item'),

    url('display_Maintainance/',display_Maintainance,name ='display_Maintainance'),
    url('display_Stiching/',display_Stiching,name ='display_Stiching'),
    url('display_Sales/', display_Sales, name ='display_Sales'),
    url('display_Weaving/',display_Weaving, name ='display_Weaving'),
    url('display_Repair/',display_Repair,name ='display_Repair'),
    
    url('registerPage/',registerPage,name ='registerPage'),

    url('signup/',signup,name ='signup'),

    url('add_item/',add_item,name ='add_item'),













]
