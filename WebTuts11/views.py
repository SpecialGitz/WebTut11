import os
import base64

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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


def geolocation_page(request):
    return render(request, 'WebTuts11/geolocation.html')

def payment_page(request):
    return render(request, 'WebTuts11/payment.html')

def canvas_page(request):
    return render(request, 'WebTuts11/canvas.html')

def audio_page (request):
    return render(request,'WebTuts11/audio.html')

def camera_capture_page(request):

        return render(request,'WebTuts11/camera_capture.html', context={}) 
    
def save_camera_image(request):

    try:
        image_data = request.POST['imageDataInput']
        image_name = request.POST['imageName']
        if image_data:
            # Decode the base64 image
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            img_data = base64.b64decode(imgstr)

            # Create a unique file name
            file_name = image_name + '.' + ext
            file_path = os.path.join(settings.BASE_DIR, 'static', 'Upload', file_name)

            # Save the image
            with open(file_path, 'wb') as f:
                f.write(img_data)

            return JsonResponse({'status': 'photo saved successfully'})
        else:
            return JsonResponse({'status': 'image data not found'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    