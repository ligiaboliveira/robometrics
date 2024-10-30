# algoritmo_genetico/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('run-genetic-algorithm/', views.run_genetic_algorithm, name='run_genetic_algorithm')
]
