from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, "hello.html", context)

context = {
    'title' : 'DJango'
}
def home(request):
    return render(request, "home.html", context)

def page(request):
    return render(request, 'hello.html')

def about(request):
    return render(request, 'about.html', context)

def base(request):
    return render(request, 'base.html', context)