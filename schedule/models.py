from django.db import models

class PlantingSchedule(models.Model):
    plant_name = models.CharField(max_length=255)
    planting_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.plant_name
