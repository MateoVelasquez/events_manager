from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('health_check', views.get_health_check, name='health_check')
]