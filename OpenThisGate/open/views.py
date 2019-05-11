from django.shortcuts import render
import script_open

def index(request):
    return render(request, 'open/index.html')   

def open(request):
    script_open.open()
    return render(request, 'open/it_is_open.html')       
