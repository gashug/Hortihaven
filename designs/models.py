from django.db import models

class GardenDesign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class GardenPlant(models.Model):
    garden_design = models.ForeignKey(GardenDesign, related_name='garden_plants', on_delete=models.CASCADE)
    plant = models.ForeignKey('garden_plants.Plant', on_delete=models.CASCADE)
    position_x = models.PositiveIntegerField(default=0)
    position_y = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.plant.name} at ({self.position_x}, {self.position_y})"