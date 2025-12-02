from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Blog 3 Home Page </h1>")   


def about(request):
    return HttpResponse("<h1>About Blog 3</h1>")    

