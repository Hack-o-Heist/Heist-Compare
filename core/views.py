from django.http.response import Http404
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .templatetags.Scrappers.amazon import amazon_products
from .templatetags.Scrappers.amazon_product import amazon_product_details
from .templatetags.Scrappers.flipkart import flipkart_products
from .templatetags.Scrappers.flipkart_product import flipkart_product_details
from django.core.cache import cache
import json
from django.views.decorators.csrf import csrf_exempt


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
        cache.set('search_'+keywords, products, timeout=None)


    keywords.capitalize()
    return render(request, 'core/search.html', {'products': products, 'keyword': keywords})


@csrf_exempt
def get_product_details(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    
    page_link = request.POST.get('link', '')

    if 'amazon.in' in page_link:
        page_details = amazon_product_details(page_link)
        return HttpResponse(json.dumps(page_details['response']), content_type="application/json")
    
    if 'flipkart.com' in page_link:
        page_details = flipkart_product_details(page_link)
        return HttpResponse(json.dumps(page_details['response']), content_type="application/json")

    return Http404()
