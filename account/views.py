from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Product
from django.contrib.auth import authenticate, login, logout

from account.models import Product
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        if User.objects.filter(username=username).exists():
            print("User Exists")
            messages.error(request, 'User already exists')
        else:
            print("User does not exist")
            user_register = User.objects.create_user(username=username, password=password)
            user_register.save()
            messages.success(request, 'User created successfully')
                
    return render(request,"register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user =authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request,"login.html")

def home(request):
    pro = Product.objects.all()
    print(pro)
    return render(request, 'home.html',{'pro': pro})
    

def edit(request):
    pro = Product.objects.all()
    print(pro)
    return render(request, 'edit.html',{'pro': pro})
    

def user_logout(request):
    logout(request)
    return redirect('login')

def add(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        description = request.POST['description'] 
        price = request.POST['price']
        offer = request.POST['offer']
        print(name, description, price, offer)
        if Product.objects.filter(name=name).exists():
            print("Product Exists")
            messages.error(request, 'Product already exists')
        else:    
                pro = Product.objects.create(name=name, description=description, price=price, offer=offer)
                pro.save()
                messages.success(request, 'Product Added successfully')
                return redirect('home')

    return render(request, 'add.html')
    
    
def  update_product(request,id):
    item=get_object_or_404(Product,id=id)
    if request.method =='POST':
        
        item.name=request.POST.get('name')
        item.description=request.POST.get('description')
        item.price=request.POST.get('price')
        item.offer=request.POST.get('offer')
        item.save()
        return redirect('home')
        print("product display")
        
    return render(request, 'update.html',{"i":item})
    
def delete_product(request,id):
    item=Product.objects.get(id=id)
    item.delete()
    return redirect('home')

    