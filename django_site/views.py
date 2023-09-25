from django.shortcuts import render

# Create your views here.
def site(request):
    return None

from django.http import HttpResponse
from django.shortcuts import render

def site(request):
    return render(request, 'site.html', {'data': "Python is Fun"})

from django.shortcuts import render

def plus(request):
    return render(request, 'plus.html')

