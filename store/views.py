from django.shortcuts import render
from django.views import View
from .models import Cart, Customer, Product, OrderPlaced


def home(request):
 return render(request, 'it_home.html')


def ServerDesktop(request, data=None):
 if data == None:
  server_desktop = Product.objects.filter(category='SD')
 elif data == 'DELL' or data == 'IBM' or data == 'HP':
  server_desktop = Product.objects.filter(category='SD').filter(brand=data)

 return render(request, 'servers_desktops.html', {'server_desktop': server_desktop})

def Laptops(request, data=None):
 if data == None:
  laptop = Product.objects.filter(category='L')
 elif data == 'DELL' or data == 'IBM' or data == 'HP':
  laptop = Product.objects.filter(category='L').filter(brand=data)

 return render(request, 'laptops.html', {'laptop': laptop})

def Mobiles(request, data=None):
 if data == None:
  mobile = Product.objects.filter(category='M')
 elif data == 'VIVO' or data == 'SAMSUNG' or data == 'TECHNO':
  mobile = Product.objects.filter(category='M').filter(brand=data)

 return render(request, 'mobiles.html', {'mobile': mobile})

def Gadgets(request, data=None):
 if data == None:
  gadget = Product.objects.filter(category='TG')
 elif data == 'GOOGLE' or data == 'SAMSUNG' or data == 'HUAWEI':
  gadget = Product.objects.filter(category='TG').filter(brand=data)

 return render(request, 'tech_gadgets.html', {'gadget': gadget})

#def product_detail(request):
 #return render(request, 'product_detail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'product_detail.html', {'product': product})