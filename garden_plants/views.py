from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Plant

def index(request):
    plants = Plant.objects.all()
    return render(request, 'garden_plants.html', {'plants': plants})

def plant_detail(request, id):
    plant = get_object_or_404(Plant, pk=id)
    print(f"Rendering details for plant: {plant.name}")
    # return HttpResponse("This is the Plant Detail Page.")
    return render(request, 'plant_detail.html', {'plant': plant})