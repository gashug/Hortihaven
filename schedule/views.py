from django.shortcuts import render
from .models import PlantingSchedule

def planting_schedule(request):
    schedules = PlantingSchedule.objects.all()
    return render(request, 'planting_schedule.html', {'schedules': schedules})
