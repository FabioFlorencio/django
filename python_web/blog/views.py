#from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    return render(
        request,
        'blog/blog.html'
    )

def exemplo(request):
    return render(
        request,
        'blog/exemplo.html'
    )