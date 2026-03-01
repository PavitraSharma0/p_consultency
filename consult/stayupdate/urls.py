from django.urls import path
from . import views

urlpatterns = [
    path('stayupdate/', views.stayupdate_view, name='stayupdate'),
]
