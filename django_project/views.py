from django.http import HttpResponse, HttpRequest

def index(request):
    return HttpResponse(request,'base.html')
