from django.shortcuts import render
from .models import Tutorial

def tutorial_list(request):
    tutorial = Tutorial.objects.all()
    return render(request, 'tutorial_list.html', {'tutorial': tutorial})
