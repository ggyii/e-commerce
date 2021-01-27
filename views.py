from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
  products = Product.objects.all()
  allProds = []
  catProds = Product.objects.values('product_cat','id')
  cats = {item['product_cat'] for item in catProds}
  for cat in cats:
    # TODO: write code...
    prod = Product.objects.filter(product_cat = cat)
    product = prod[0:3]
    allProds.append([product, cat, range(1,len(products))])
  params={'product':products,'allProds':allProds,'products':product}
  return render(request,'shop/index.html',params)
def category(request,slug):
  
  allProds = []
  catProds = Product.objects.values('product_cat','id')
  cats = {item['product_cat'] for item in catProds}
  for cat in cats:
    # TODO: write code...
    prod = Product.objects.filter(product_cat = cat)
    
    allProds.append([prod, cat, slug])
  params={'allProds':allProds,'products':prod,'q':cat}
  return render(request,'shop/cat.html',params)
def about(request):
	return render(request,'shop/index.html')
def contact(request):
	return render(request,'shop/index.html')
def tracker(request):
	return render(request,'shop/index.html')
def search(request):
	return render(request,'shop/index.html')
def checkout(request):
	return render(request,'shop/index.html')
def prodview(request,pr_id):
	product = Product.objects.filter(id = pr_id)
	print(product)
	
	return render(request,'shop/prodview.html', {'product':product[0]})