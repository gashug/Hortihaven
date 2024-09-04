from django.urls import path
from . import views

urlpatterns = [
        path('index', views.index, name='index'),
        path('designs/', views.garden_design_list, name='garden_design_list'),
        path('<int:pk>/', views.garden_design_detail, name='garden_design_detail'),
]
