from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('decode/', views.decode),
    path('encode/', views.encode)
]