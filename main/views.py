from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'E-Ndomaret',  
        'my_name': 'Muhammad Daffa Abyaz Tjiptadi',        
        'my_class': 'PBP A',      
    }
    return render(request, "main.html", context)

