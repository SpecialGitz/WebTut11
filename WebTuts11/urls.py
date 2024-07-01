from django.urls import path

from . import views

urlpatterns = [
    path("camera/",views.camera_page,name="camera"),
    path("",views.index,name=""),
    path("audio/",views.audio_page,name="audio" )
]