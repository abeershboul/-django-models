from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Snack

# Create your views here.
class HomePage(TemplateView):
    template_name= 'home.html'
class About(TemplateView):
    template_name= 'about.html'  
class Snacks(ListView):
    template_name = 'snack_list.html' 
    model =  Snack   