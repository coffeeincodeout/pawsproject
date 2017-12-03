from django.urls import path

from . import views

urlpatterns = [
    path('pets', views.index, name='index'),
]