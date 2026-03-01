from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='blog'),
    path('detail/', views.detail_view, name='detail'),
    path('feature/', views.feature_view, name='feature'),
    path('quote/', views.quote_view, name='quote'),
    path('team/', views.team_view, name='team'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
]