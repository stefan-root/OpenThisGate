from django.shortcuts import render
import logger
import script_open

def index(request):
    return render(request, 'open/index.html')   

def open(request):
    logger.log('Opening gate for ' + request.META['REMOTE_ADDR'])
    script_open.open()
    return render(request, 'open/it_is_open.html')       
