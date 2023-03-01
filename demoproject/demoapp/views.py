from django.shortcuts import render

from .models import Place, Team


# Create your views here.
def demo(request):
    obj1=Place.objects.all()
    obj=Team.objects.all()
    return render(request, "index.html",{'result':obj1,'result2':obj})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
