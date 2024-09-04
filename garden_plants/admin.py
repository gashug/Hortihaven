from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'description', 'sunlight_requirements', 'water_requirements', 'soil_requirements', 'planting_season', 'harvest_time')
    search_fields = ('name', 'family', 'description')
    list_filter = ('family', 'sunlight_requirements', 'water_requirements', 'soil_requirements', 'planting_season', 'harvest_time')
