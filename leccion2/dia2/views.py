from django.shortcuts import render
from .models import Producto
# Create your views here.
def index(request):
    return render(request,'dia2/index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'dia2/productos.html', {'productos': productos})
