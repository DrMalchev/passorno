#from asyncio.windows_events import NULL
from django.urls import path
from . import views
#from django.conf import settings 
#from django.conf.urls.static import static 
from django.shortcuts import render

urlpatterns = [
    path("", views.index, name="index"),
    path("fileupload", views.fileupload, name="fileupload"),
    #path("startCalc", views.startCalc, name="startCalc"),
    path("results", views.results, name="results"),
]