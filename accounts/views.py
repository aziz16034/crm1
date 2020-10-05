from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import *




# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact_us(request):
    return render(request,'contact_us.html')


def about(request):
    return HttpResponse('about')


def product_item(request):
    return render(request,'product_item.html')

def display_Maintainance(request):
    items = Maintainance.objects.all()
    context = {
        'items' : items,
        'context': 'Maintainance'
    }

    return render(request, 'product_item.html', context)


def display_Repair(request):
    items = Repair.objects.all()
    context = {
        'items' : items,
        'context': 'Repair'
    }

    return render(request, 'product_item.html', context)



def display_Stiching(request):
    items = Stiching.objects.all()
    context = {
        'items' : items,
        'context': 'Stiching'
    }

    return render(request, 'product_item.html', context)
    


def display_Sales(request):
    items = Sales.objects.all()
    context = {
        'items' : items,
        'context': 'Sales'
    }

    return render(request, 'product_item.html', context)


def display_Weaving(request):
    items = Weaving.objects.all()
    context = {
        'items' : items,
        'context': 'Weaving'
    }

    return render(request, 'product_item.html', context)

def registerPage(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'product_item.html', context)

    


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_item')
    context = {}
    return render(request, 'loginPage.html')



def add_item(request, cls):
    if request.method =="POST":
        form = cls(request.POST)
        
        if form.is_valid():
            form.save
            return redirect('product_item')




    else:
        form = cls()
        return render(request,'add_new.html', {'form': form} )



def add_repair(request):
    return add_item(request, RepairForm)


def add_stiching(request):
    return add_item(request, StichingForm)


def add_weaving(request):
    return add_item(request, WeavingForm)


def add_maintain(request):
    return add_item(request, MaintainForm)


def add_sales(request):
    return add_item(request, SalesForm)




def demo(request):
    return render(request, 'demo.html')







