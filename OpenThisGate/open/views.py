from django.shortcuts import render
from script_open import open

def index(request):
    return render(request, 'open/index.html')   

def open(request):
    open()
    return render(request, 'open/it_is_open.html')       
