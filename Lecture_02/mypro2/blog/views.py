from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog_home(request):

    a = 10
    b = 20
    sum = a + b
    return HttpResponse(f"The sum of {a} and {b} is {sum}")



