from bs4 import BeautifulSoup
import requests


def amazon_products(keywords):
    keywords = keywords.replace(' ', "%20")

    try:
        r = requests.get(f'https://www.amazon.in/s?k={keywords}')

        while r.status_code != 200:
            print(r)
            r = requests.get(f'https://www.amazon.in/s?k={keywords}')


        soup = BeautifulSoup(r.text, 'html.parser')

        all_items = soup.findAll("div", attrs={'data-component-type': 's-search-result'})
    
        products = []

        for item in all_items:
            try:
                link = "https://www.amazon.in" + item.find("a", attrs={'class': 'a-link-normal'})['href']
                img = item.find("img", attrs={'class': 's-image'})['src']
                title = item.find("span", attrs={'class': 'a-size-medium a-color-base a-text-normal'}).text
                rating = item.find("span", attrs={'class': 'a-icon-alt'}).text.split(" ")[0]
                price = item.find("span", attrs={'class': 'a-offscreen'})

                if price:
                    price = price.text
                
                product = {
                    'link': link,
                    'img': img,
                    'title': title,
                    'price': price, 
                    'rating': rating
                }
                
                products.append(product)
            except Exception as e:
                print(e)
        
        return {'type': 'success', 'products': products}

    except Exception as e:
        print("error in amazon", e)
        return {'type': 'error', 'error': e}


if __name__ == '__main__':
    print(amazon_products('Laptops bags'))
