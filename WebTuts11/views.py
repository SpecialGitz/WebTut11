from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("Hello, world. You're at the main page index.")

def camera_page (request):
    return render(request,'WebTuts11/camera.html',{})

def audio_page (request):
    return render(request,'WebTuts11/audio.html',{})