from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')


def video(request):
    return render(request, 'core/video.html')

