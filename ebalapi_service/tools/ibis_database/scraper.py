from typing import NamedTuple

import bs4
import requests
import json
from tqdm import trange, tqdm


class BulletTuple(NamedTuple):
    name: str
    vendor: str
    diameter: float
    weight: float
    length: float
    g1: float
    g7: float


class CartridgeTuple(NamedTuple):
    ...


BASE_URL = 'https://ibis.net.ua/ua'


def scrap_cartridges(offset=''):
    response = requests.get(f'{BASE_URL}/products/patrony-nareznye86/{offset}')
    html = response.text

    # print(html)

    soup = bs4.BeautifulSoup(html)
    products = soup.find_all('a', {"class": "pb_product_name"}, href=True)
    # products_links = [f"{BASE_URL}{p['href']}" for p in products]
    products_links = [p['href'] for p in products]
    return products_links


def get_all_cartridges(max_offset: int = 700):
    prods = scrap_cartridges()
    for i in trange(20, max_offset + 20, 20):
        carts = scrap_cartridges(f'offset{i}')
        if carts:
            prods += carts
    return prods


def scrap_cartridge(url: str):
    uri = f'{BASE_URL}{url}#pane_ttx'
    response = requests.get(uri)
    soup = bs4.BeautifulSoup(response.text)

    # prod = soup.find('meta', itemprop="description")
    # ttx = [tx.strip() for tx in prod['content'].split('/')]
    # print(ttx)

    product_name = soup.find('h1', {"class", "product_name"})

    ttx = soup.find('div', {"class": "pane_ttx"})
    ttx = ttx.find_all('tr')
    ttx_dict = {
        "product_name": product_name.text if product_name else None,
        "vendor": None,
        "caliber": None,
        "muzzle_velocity": None,
        "bc": None,
        "bullet_name": None,
        "energy": None,
        "weight": None,
        'url': uri,
        "tags": []
    }
    for tx in ttx:
        tags = [tag.text.replace(u'\xa0', u' ').replace(u'\n', u' ').strip() for tag in tx.find_all()]
        # print(tags, 'Виробник:' in tags)

        ttx_dict['tags'].append(tags)

        if 'Виробник:' in tags:
            ttx_dict['vendor'] = tags[-1]
        elif 'Калібр:' in tags:
            ttx_dict['caliber'] = tags[-1]
        elif 'Початкова швидкість, м/с:' in tags:
            ttx_dict['muzzle_velocity'] = tags[-1]
        elif 'Назва кулі:' in tags:
            ttx_dict['bullet_name'] = tags[-1]
        elif 'БК кулі:' in tags:
            ttx_dict['bc'] = tags[-1]
        elif 'Енергія, Дж:' in tags:
            ttx_dict['energy'] = tags[-1]
        elif 'Маса кулі:' in tags:
            ttx_dict['weight'] = tags[-1]

    # print(len(ttx_dict['tags']), ttx_dict)

    return ttx_dict

    # cart = CartridgeTuple(
    #     name=product_name.text,
    #     bullet_name=tags[9][2],
    #     caliber=[5][2],
    #     weight=tags[12][2],
    #     velocity=[7][2],
    #     bc='',
    #     energy=tags[10][2],
    # )


if __name__ == '__main__':
    carts = get_all_cartridges(700)
    cl = [scrap_cartridge(cart) for cart in tqdm(carts)]
    with open('carts.json', 'w') as fp:
        json.dump(cl, fp)
