from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homeView(request):
    context = {}
   
    return render(request, 'index.html',context)
