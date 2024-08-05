from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cofee

def home(request):
    cofee = Cofee.objects.all()
    return render(request,'home.html',{'cofee':cofee})