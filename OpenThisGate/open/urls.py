from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('it_is_open', views.open, name='it_is_open'),
]