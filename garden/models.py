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

class GardenDesign(models.Model):
    name = models.CharField(max_length=255)
    layout = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InspirationGallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PlantingSchedule(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    due_date = models.DateField()
    reminder = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plant.name} - {self.task}"
