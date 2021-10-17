from bs4 import BeautifulSoup
import requests


def amazon_product_details(link):
    try:
        r = requests.get(link)

        while r.status_code != 200:
            print(r)
            r = requests.get(link)


        soup = BeautifulSoup(r.text, 'html.parser')

        table_rows = soup.find("table", attrs={'id': 'productDetails_techSpec_section_1'}).find_all('tr')

        response = {}

        for row in table_rows:
            try:
                key = str(row.find('th').text).replace('\n', '').replace('\u200e', '')
                value = str(row.find('td').text).replace('\n', '').replace('\u200e', '')
                response[key] = value
            except Exception as e:
                print(e)
        
        return {'type': 'success', 'response': response}

    except Exception as e:
        print("error in amazon", e)
        return {'type': 'error', 'error': e}


if __name__ == '__main__':
    print(amazon_product_details("https://www.amazon.in/Avita-Cosmos-Celeron-Dual-Core/dp/B09HKBR46P"))
