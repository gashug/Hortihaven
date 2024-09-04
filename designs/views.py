from django.shortcuts import render, get_object_or_404
from .models import GardenDesign

def index(request):
    return render(request, 'garden_design.html')

def garden_design_list(request):
    designs = GardenDesign.objects.all()
    return render(request, 'garden_design_list.html', {'designs': designs})

def garden_design_detail(request, pk):
    design = get_object_or_404(GardenDesign, pk=pk)
    return render(request, 'garden_design_detail.html', {'design': design})

