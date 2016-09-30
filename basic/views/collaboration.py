from django.shortcuts import render
from django.http import HttpResponse

def collaboration(request):
    return render(request, 'basic/collaboration.html', {})
