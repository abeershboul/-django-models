from django.urls import path,include
from .views import HomePage ,About,Snacks

urlpatterns = [
    path('home',HomePage.as_view(),name='home'),
    path('about',About.as_view(),name='about'),
    path('',Snacks.as_view(),name='snacks')
    
    
]