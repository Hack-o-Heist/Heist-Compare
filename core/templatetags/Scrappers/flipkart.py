from bs4 import BeautifulSoup
import requests


def flipkart_products(keywords):
    keywords = keywords.replace(' ', "%20")

    try:
        r = requests.get(f'https://www.flipkart.com/search?q={keywords}')

        while r.status_code != 200:
            print(r)
            r = requests.get(f'https://www.flipkart.com/search?q={keywords}')


        soup = BeautifulSoup(r.text, 'html.parser')
        print(r)

        all_items = soup.findAll("div", attrs={'class': '_1YokD2 _3Mn1Gg'})[-1]

        print(len(all_items))

        products = []

        for item in all_items:
            if item.__contains__("<span>Ad</span>"):
                print('a')
                continue
            
            try:
                link = "https://www.flipkart.com" + item.find("a", attrs={'class': '_1fQZEK'})['href']
                img = item.find("img", attrs={'class': '_396cs4 _3exPp9'})['src']
                title = item.find("div", attrs={'class': '_4rR01T'}).text
                rating = item.find("div", attrs={'class': '_3LWZlK'}).text.split(" ")[0]
                price = item.find("div", attrs={'class': '_30jeq3 _1_WHN1'})

                if price:
                    price = price.text
                
                if not price:
                    continue

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
        return {'type': 'error', 'error': e}


if __name__ == '__main__':
    print(flipkart_products('keyboard'))
