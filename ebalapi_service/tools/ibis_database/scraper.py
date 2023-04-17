import re
from typing import NamedTuple

import bs4
import requests
import json
from tqdm import trange, tqdm
import logging

logging.basicConfig(filename='scrap.log', filemode='w')
log = logging.getLogger('scrapper')


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

    soup = bs4.BeautifulSoup(html, features="lxml")
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

    # print(uri, response)
    soup = bs4.BeautifulSoup(response.text, features="lxml")

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
        "g7": None,
        "bullet_name": None,
        # "energy": None,
        "weight": None,
        'url': uri,
        # "tags": []
    }
    for tx in ttx:
        tags = [tag.text.replace(u'\xa0', u' ').replace(u'\n', u' ').strip() for tag in tx.find_all()]
        # print(tags, 'Виробник:' in tags)

        # ttx_dict['tags'].append(tags)

        if 'Виробник:' in tags:
            ttx_dict['vendor'] = tags[-1]
        elif 'Калібр:' in tags:
            ttx_dict['caliber'] = tags[-1]
        elif 'Початкова швидкість, м/с:' in tags:
            mv = re.match(r'\d?[\.,]?\d+', tags[-1])
            if mv:
                ttx_dict['muzzle_velocity'] = float(mv.group(0).replace(',', '.'))
        elif 'Назва кулі:' in tags:
            ttx_dict['bullet_name'] = tags[-1]
        elif 'БК кулі:' in tags:

            matches = re.findall(r'\d?[\.,]?\d+', tags[-1])
            if matches:
                matches = [m for m in matches if m not in ['7', '1']]

                matches.sort(reverse=True)

                # print(len(matches), matches, uri)
                try:
                    val = float(matches[0].replace(',', '.'))
                    if val > 1:
                        raise ValueError
                    ttx_dict['bc'] = val

                    if len(matches) > 1:
                        try:
                            val = float(matches[1].replace(',', '.'))
                            if val > 1:
                                raise ValueError
                            ttx_dict['g7'] = val
                        except ValueError:
                            ttx_dict['g7'] = float(input('enter g7'))

                except ValueError:

                    log.error(uri)
                    # ttx_dict['bc'] = float(input('enter g1'))
                    # ttx_dict['g7'] = float(input('enter g7'))


        # elif 'Енергія, Дж:' in tags:
        #     ttx_dict['energy'] = tags[-1]
        elif 'Маса кулі:' in tags:
            matches = re.findall(r'\d?[\.,]?\d+', tags[-1])
            if matches:
                matches.sort(reverse=True)
                ttx_dict['weight'] = float(matches[0].replace(',', '.'))

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
    # carts = get_all_cartridges(700)
    #
    # with open('prods.json', 'w', encoding='utf-8') as fp:
    #     json.dump(carts, fp, ensure_ascii=False)

    with open('prods.json', 'r', encoding='utf-8') as fp:
        carts = json.load(fp)

    cl = [scrap_cartridge(cart) for cart in tqdm(carts)]

    with open('carts-utf.json', 'w', encoding='utf-8') as fp:
        json.dump(cl, fp, ensure_ascii=False)

    # with open('carts.json', 'r') as fp:
    #     data = json.load(fp)
    #
    # with open('carts.json', 'w', encoding='utf-8') as fp:
    #     json.dump(data, fp, ensure_ascii=False)
