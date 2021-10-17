from django.shortcuts import render
from .templatetags.Scrappers.amazon import amazon_products
from .templatetags.Scrappers.flipkart import flipkart_products
from django.core.cache import cache


# Create your views here.
def index(request):
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')


def video(request):
    return render(request, 'core/video.html')

def about(request):
    return render(request, 'core/about.html')



def search(request, keywords):
    products = cache.get('search_'+keywords, [])

    if len(products) == 0:
        amazon_product = amazon_products(keywords)
        if amazon_product['type'] == 'success':
            products = products + amazon_product['products']

        flipkart_product = flipkart_products(keywords)
        if flipkart_product['type'] == 'success':
            products = products + flipkart_product['products']
        
        products = sorted(products, key=lambda p: float(str(p['price']).replace(',', '').replace("₹", '')))
        cache.set('search_'+keywords, products)


    keywords.capitalize()
    return render(request, 'core/search.html', {'products': products, 'keyword': keywords})
