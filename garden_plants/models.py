from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    description = models.TextField()
    sunlight_requirements = models.CharField(max_length=255, null=True, blank=True)
    water_requirements = models.CharField(max_length=255, null=True, blank=True)
    soil_requirements = models.CharField(max_length=255, null=True, blank=True)
    planting_season = models.CharField(max_length=255, null=True, blank=True)
    harvest_time = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
