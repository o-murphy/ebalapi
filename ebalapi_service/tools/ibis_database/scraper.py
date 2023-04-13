import requests
import bs4


BASE_URL = 'https://ibis.net.ua'


def scrap_bulletts(offset=''):
    response = requests.get(f'{BASE_URL}/products/patrony-nareznye86/{offset}')
    html = response.text

    # print(html)

    soup = bs4.BeautifulSoup(html)
    products = soup.find_all('a', {"class": "pb_product_name"}, href=True)
    products_links = [f"{BASE_URL}{p['href']}" for p in products]
    return products_links


if __name__ == '__main__':

    prods = scrap_bulletts()

    for i in range(20, 100, 20):
        carts = scrap_bulletts(f'offset{i}')
        if carts:
            prods += carts

    print(prods, len(prods))

