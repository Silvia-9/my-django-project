from django.urls import path
from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.home, name='home'),
    path('clear-expenses/', views.clear_expenses, name='clear_expenses'),
    path('calculate-total/', views.calculate_total, name='calculate_total'),
]

