from django.urls import path
from .views import SnackListView,SnackDetail,HomePage,AboutPage
urlpatterns = [
    path('',SnackListView.as_view(),name='snacks'),
    path('<int:pk>',SnackDetail.as_view(),name='detail'),
    path('home', HomePage.as_view(),name='home'),
    path('about/', AboutPage.as_view(),name='about')
]  
    
