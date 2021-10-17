from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('search/<str:keywords>', views.search, name="search"),
    path('about', views.about, name="about"),
    path('video', views.video, name="video"),
    path('contact', views.contact, name="contact"),
]
