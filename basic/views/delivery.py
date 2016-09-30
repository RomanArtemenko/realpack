from django.shortcuts import render
from django.http import HttpResponse

def delivery(request):
    return render(request, 'basic/delivery.html', {})
