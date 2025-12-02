from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Shop  Home Page </h1>")   


def products(request):
    return HttpResponse("<h1>product Shop page </h1>")    

