from django.shortcuts import render
from .templatetags.Scrappers.amazon import amazon_products
from .templatetags.Scrappers.flipkart import flipkart_products


# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')


def video(request):
    return render(request, 'core/video.html')

def search(request, keywords):
    products = []
    amazon_product = amazon_products(keywords)
    if amazon_product['type'] == 'success':
        products = products + amazon_product['products']
    flipkart_product = flipkart_products(keywords)
    if flipkart_product['type'] == 'success':
        products = products + flipkart_product['products']

    products = {i:k for i, k in enumerate(products)}
    return render(request, 'core/home.html', {'products': products})
