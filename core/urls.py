from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('video', views.video, name="video"),
    path('contact', views.contact, name="contact"),
]
