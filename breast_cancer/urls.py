from django.urls import path
from . import views

app_name = 'breast_cancer'

urlpatterns = [
    path('', views.breast_cancer, name='breast_cancer'),
    path('result/', views.result, name='result'),
]
