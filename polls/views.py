from django.shortcuts import render
from .models import Question, choice

# Get questions and display them

def index(request):
    return render(request, 'polls/index.html')
