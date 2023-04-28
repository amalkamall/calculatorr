from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"add.html",{"out":result})
        
class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        return render(request,"sub.html",{"res":result})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        return render(request,"mul.html",{"mul":result})
        
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        f=1
        n=int(n1)
        for i in range(1,n+1):
            f= f*i
        result=f
        return render(request,"fact.html",{"fact":result})

class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n=int(n1)
        f=1
        IsPrime=True
        for i in range(2,n):
            if n%i==0:
                IsPrime=False
                break
        return render(request,"prime.html",{"prime":IsPrime})
        
class IndexView(View):
    def get(sef,request,*args,**kwargs):
        return render(request,"index.html")
