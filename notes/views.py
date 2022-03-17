from django.shortcuts import render
from .models import Note


def index(request):
    if request.method == 'POST':
        print("lol")
    all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})