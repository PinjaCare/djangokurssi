from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

# Product view´s

def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render (request,"productlist.html",context)

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request, "supplierlist.html",context)
