from django.db import models

class InspirationGallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='inspiration_images/')  # Assuming you store images

    def __str__(self):
        return self.title
