from django.urls import path

from . import views

urlpatterns = [
    path("camera/",views.camera_page,name="camera_page"),
    path("capture/",views.camera_capture_page,name="camera_capture_page"),
    path("save_camera_image/",views.save_camera_image,name="save_camera_image"),
    path("",views.index,name=""),
    path("audio/",views.audio_page,name="audio"),
]