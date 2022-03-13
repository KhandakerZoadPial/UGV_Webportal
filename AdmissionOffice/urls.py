from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.custom_reg, name='reg')
]