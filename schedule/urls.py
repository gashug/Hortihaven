from django.urls import path
from . import views

urlpatterns = [
    path('', views.planting_schedule, name='planting_schedule'),
]
