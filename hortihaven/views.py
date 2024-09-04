from django.shortcuts import render

# View function to render the homepage
def index(request):
    return render(request, 'index.html')
