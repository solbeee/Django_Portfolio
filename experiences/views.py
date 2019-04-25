from django.shortcuts import render
from .models import Experiences

# Create your views here.
def resume(request):
    experiences = Experiences.objects
    return render(request, 'experiences/resume.html', {'experiences':experiences})
