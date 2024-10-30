from django.urls import path
from . import views

urlpatterns = [
    path('', views.corridas, name='corridas'),
    path('create_pid', views.create_pid, name='create_pid'),
    path('upload/', views.upload_file, name='upload_file')
]