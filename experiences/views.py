from django.shortcuts import render, get_object_or_404
from .models import Experiences

# Create your views here.
def resume(request):
    experiences = Experiences.objects
    return render(request, 'experiences/home.html', {'experiences':experiences})

def detail(request, experiences_id):
    experiences.detail = get_object_or_404(Experiences, pk=experiences_id)
    return render(request, 'experiences/detail.html', {'experiences':experiences_detail})
