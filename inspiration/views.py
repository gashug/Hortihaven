from django.shortcuts import render
from .models import InspirationGallery

def inspiration_gallery(request):
    inspirations = InspirationGallery.objects.all()
    return render(request, 'inspiration_gallery.html', {'inspirations': inspirations})
