from django.urls import path
from news import views




urlpatterns = [
    path('', views.home, name='index'),
    path('catagory', views.catagory, name='catagory'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('singlepost', views.singlepost, name='singlepost'),
    
]