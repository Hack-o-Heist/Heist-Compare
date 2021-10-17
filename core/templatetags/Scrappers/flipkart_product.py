from bs4 import BeautifulSoup
import requests


def flipkart_product_details(link):
    try:
        r = requests.get(link)

        while r.status_code != 200:
            print(r)
            r = requests.get(link)


        soup = BeautifulSoup(r.text, 'html.parser')

        all_tables = soup.find_all("table", attrs={'class': '_14cfVK'})

        response = {}

        for table in all_tables:
            table_rows = table.find_all('tr')


            for row in table_rows:
                try:
                    key = row.find_all('td')[0].text
                    value = row.find_all('td')[1].text
                    response[key] = value
                except Exception as e:
                    print(e)
            
            return {'type': 'success', 'response': response}

    except Exception as e:
        print("error in flipkat product", e)
        return {'type': 'error', 'error': e}


if __name__ == '__main__':
    print(flipkart_product_details("https://www.flipkart.com/lenovo-apu-dual-core-a9-a99425-4-gb-1-tb-hdd-dos-e41-45-notebook/p/itm910e1083480e9?pid=COMG4J4JH4QRPXGM&lid=LSTCOMG4J4JH4QRPXGMZQHALZ&marketplace=FLIPKART&q=laptop&store=6bo%2Fb5g&srno=s_1_17&otracker=search&fm=organic&iid=2c746f2b-8a81-42e5-9939-1ff522279fc4.COMG4J4JH4QRPXGM.SEARCH&ppt=None&ppn=None&ssid=9unzs0lzy80000001634480090238&qH=312f91285e048e09"))
