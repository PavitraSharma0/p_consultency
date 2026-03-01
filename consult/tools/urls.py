from django.urls import path
from .import views

urlpatterns = [
    path('', views.tools_dashboard, name='tools_dashboard'),
]