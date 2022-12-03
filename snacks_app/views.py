from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Snack

# Create your views here.
# class HomePage(TemplateView):
#     template_name= 'home.html'
# class About(TemplateView):
#     template_name= 'about.html'  
# class Snacks(ListView):
#     template_name = 'snack_list.html' 
#     model =  Snack   
# class SnackDetail(DetailView):
#     model=Snack
#     template_name='snack_detail.html'    

from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from .models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

class SnackDetail(DetailView):
    model=Snack
    template_name='snack_detail.html'
class HomePage(TemplateView):
    template_name = 'home.html'
class AboutPage(TemplateView):
    template_name = 'about.html'    