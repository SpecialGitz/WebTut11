from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name=""),
    path("camera/",views.camera_page,name="camera_page"),
    path("capture/",views.camera_capture_page,name="camera_capture_page"),
    path("save_camera_image/",views.save_camera_image,name="save_camera_image"),
    path("audio/",views.audio_page,name="audio"),
    path("geolocation/",views.geolocation_page,name="geolocation"),
    path("payment/",views.payment_page,name="payment"),
    path("canvas/",views.canvas_page,name="canvas"),
]