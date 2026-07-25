from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfume_list, name='perfume_list'),
]