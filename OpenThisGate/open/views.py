from django.shortcuts import render

def index(request):
    return render(request, 'open/index.html')   

def open(request):
    return render(request, 'open/it_is_open.html')       