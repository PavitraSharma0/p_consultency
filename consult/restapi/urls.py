from django.urls import path
from . import views

urlpatterns = [

    path('tax-consultancy/', views.tax_consultancy_page, name='tax_consultancy'),
    path('api/tax-advice/', views.tax_advice_api, name='tax_advice_api'),
]