from django.urls import path
from . import views

urlpatterns = [
    path('', views.robos, name='robos'),
    path('create_robos', views.create_robos, name='create_robos')
]
