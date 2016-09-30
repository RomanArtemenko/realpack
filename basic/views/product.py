from django.shortcuts import render
from django.http import HttpResponse

def product(request):
#    return HttpResponse('<h1>Product Page/h1>')
    return render(request, 'basic/product.html', {})
