from django.urls import path
from dia2 import views

urlpatterns = [
    path('',views.index, name='home'),
    path('producto/', views.productos,name='productos')
]