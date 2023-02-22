from django.shortcuts import render
from .models import Pizza

# Create your views here.
def home(request):
    return render(request,"pizzas/home.html")

def pizzas(request):
    pizzas=Pizza.objects.all()
    
    context={
        "pizzas":pizzas
    }
    
    return render(request,"pizzas/pizzas.html",context)

def order_view(request,id):
    pizza=Pizza.objects.get(id=id)
    
    context={
        "pizza":pizza
    }
    
    return render(request,"pizzas/order.html",context)