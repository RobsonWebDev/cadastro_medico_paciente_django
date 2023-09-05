from django.urls import path
from cadastro import views

urlpatterns = [
    path("", views.index, name = 'index'),
]