import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse

from WebTut11 import settings
from .forms import ImageUploadForm


# Create your views here.
def index (request):
    return HttpResponse("Hello, world. You're at the main page index.")

def camera_page (request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = request.FILES["image"]

            _, file_extension = os.path.splitext(img.name)

            upload_dir = os.path.join(settings.BASE_DIR, 'static', 'Upload')

        file_path = os.path.join(upload_dir, name + file_extension)
        with open(file_path, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)

    else:
        form = ImageUploadForm()

    context = {'form': form}
    return render(request,'WebTuts11/camera.html', context)

def audio_page (request):
    return render(request,'WebTuts11/audio.html',{})