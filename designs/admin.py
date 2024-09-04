from django.contrib import admin
from .models import GardenDesign, GardenPlant

@admin.register(GardenDesign)
class GardenDesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')

@admin.register(GardenPlant)
class GardenPlantAdmin(admin.ModelAdmin):
    list_display = ('garden_design', 'plant', 'position_x', 'position_y')
    search_fields = ('garden_design__name', 'plant__name')