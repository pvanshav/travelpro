from django.shortcuts import render
from . models import Place,Place1
# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=Place1.objects.all()
    return render(request,"index.html",{'tab' : obj,'tab1' : obj1})

def about(request):
    return render(request,"about.html")
