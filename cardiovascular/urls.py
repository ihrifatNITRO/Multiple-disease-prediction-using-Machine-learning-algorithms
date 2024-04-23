from . import views
from django.urls import path, include

app_name = 'cardiovascular'

urlpatterns = [
    path('', views.cvd, name='cvd'),
    path('result/', views.result, name='result'),
]
