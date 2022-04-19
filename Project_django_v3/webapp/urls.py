from django.urls import path
from . import views
urlpatterns = [

    path('', views.welcome,name='Homepage'),
    path('menu.html/',views.menu,name='menu'),

]