from django.shortcuts import render,HttpResponse
from app.forms import custfm,profm
from django import views
from .models import customer,product

# Create your views here.

def cusinsert(request):
    var=custfm()
    if request.method=='POST':
        a=custfm(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse('data stored in customer table')
    return render(request,'insert.html',{'var':var})

def proinsert(request):
    var=profm()
    if request.method=='POST':
        a=profm(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse("data stored in product table")
    return render(request,'insert.html',{'var':var})

#class based views

# class pinsert(views.View):
#     def get(self,request):
#         var=profm()
#         return render(request,'insert.html',{'var':var})
#     def post(self,request):
#         a=profm(request.POST)
#         if a.is_valid():
#             a.save()
#             return HttpResponse('data stored in product table')

class crd(views.View):
    def get(self,request,pk):
        v=customer.objects.get(id=pk)
        return render(request,'read.html',{'var':v})
    
class pr(views.View):
    def get(self,request,pk):
        v=product.objects.get(id=pk)
        return render(request,'pread.html',{'var':v})
    
class cup(views.View):
    def get(self,request,pk):
        v=customer.objects.get(id=pk)
        var=custfm(instance=v)
        return render(request,'insert.html',{'var':var})
    def post(self,request,pk):
        v=customer.objects.get(id=pk)
        a=custfm(request.POST,instance=v)
        if a.is_valid():
            a.save()
            return HttpResponse('data updated in customer table')
        
class pup(views.View):
    def get(self,request,pk):
        v=product.objects.get(id=pk)
        var=profm(instance=v)
        return render(request,'insert.html',{'var':var})
    def post(self,request,pk):
        v=product.objects.get(id=pk)
        a=profm(request.POST,instance=v)
        if a.is_valid():
            a.save()
            return HttpResponse('data updated in product table')
