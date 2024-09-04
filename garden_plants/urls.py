from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Example view
    path('plant/<int:id>/', views.plant_detail, name='plant_detail'),
]