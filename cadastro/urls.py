from django.urls import path
from cadastro import views

app_name = 'cadastro'

urlpatterns = [
    path("signup/", views.signup, name = 'signup'),
    path("login/", views.login, name = 'login'),
    path("", views.index, name = 'index'),
]