import csv
import os
import re
import traceback
from typing import NamedTuple

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ebalapi.settings')
django.setup()

# Now you can access Django settings

from ebalapi_service.models import *


class BulletTuple(NamedTuple):
    id: int
    name: str
    vendor: str
    vendor_id: int
    diameter: float
    diameter_id: int
    weight: float
    g1: float
    length: float
    speed: float
    bc2: float
    speed2: float
    bc3: float
    speed3: float
    bc4: float
    speed4: float
    bc5: float
    speed5: float


class Bullet7Tuple(NamedTuple):
    id: int
    name: str
    vendor: str
    vendor_id: int
    diameter: float
    diameter_id: int
    weight: float
    length: float
    g7: float


def get_bullets() -> list[BulletTuple]:
    with open('bullets.csv', 'r') as fp:
        data = csv.reader(fp, delimiter=',')
        bullets = [BulletTuple(*row) for row in data]
    return bullets


def get_bullets7() -> list[Bullet7Tuple]:
    with open('bullets7.csv', 'r') as fp:
        data = csv.reader(fp, delimiter=',')
        bullets = [Bullet7Tuple(*row) for row in data]
    return bullets


def get_vendors_by_bullet(bullets: list[BulletTuple]) -> list[str]:
    vendor_names_list = []

    for b in bullets:
        if b.vendor not in vendor_names_list:
            vendor_names_list.append(b.vendor)
    return vendor_names_list


def add_vendors_to_db(vendors: list[str]) -> None:
    for v in vendors:
        exists = Vendor.objects.filter(name=v)
        if exists.count() == 0:
            new_vendor = Vendor.objects.create(name=v)
            print(new_vendor)


def get_diameters_by_bullet(bullets: list[BulletTuple]) -> list[float]:
    diameters_list = []

    for b in bullets:
        if b.diameter not in diameters_list:
            diameters_list.append(b.diameter)
    return diameters_list


def add_diameters_to_db(diameters: list[float]) -> None:
    for d in diameters:
        exists = Diameter.objects.filter(diameter=d)
        if exists.count() == 0:
            new_diameter = Diameter.objects.create(diameter=d)
            print(new_diameter)


def find_multibc(bullet: BulletTuple) -> (list[dict[float, float]], bool):
    print(bullet.speed2, bullet.bc2)
    if (float(bullet.speed2) > 0 and float(bullet.bc2) > 0) or (float(bullet.speed3) > 0 and float(bullet.bc3) > 0) or (
            float(bullet.speed4) > 0 and float(bullet.bc4) > 0) or (float(bullet.speed5) > 0 and float(bullet.bc5) > 0):
        return [
                   {'v': float(bullet.speed), 'bc': float(bullet.g1)},
                   {'v': float(bullet.speed2), 'bc': float(bullet.bc2)},
                   {'v': float(bullet.speed3), 'bc': float(bullet.bc3)},
                   {'v': float(bullet.speed4), 'bc': float(bullet.bc4)},
                   {'v': float(bullet.speed5), 'bc': float(bullet.bc5)},
               ], True
    return [], False


def create_multibc(bullet: Bullet, mbc: list[dict[float, float]]) -> None:
    new_df = DragFunction.objects.create(
        name=bullet.name,
        bullet=bullet,
        df_type=DragFunction.DragFunctionType.G1_MULTI_BC,
        df_data=mbc,
        comment='default',
    )
    print(new_df)


def add_bullets(bullets: list[BulletTuple]) -> None:
    for b in bullets:
        v = b.vendor
        vendor = Vendor.objects.filter(name=v).first()
        diameter = Diameter.objects.filter(diameter=b.diameter).first()

        exists = Bullet.objects.filter(name=b.name)
        if exists.count() == 0:

            try:
                new_bullet = Bullet.objects.create(
                    name=b.name,
                    vendor=vendor,
                    weight=float(b.weight),
                    length=float(b.length),
                    g1=float(b.g1),
                    g7=None,
                    diameter=diameter,
                    comment='default',
                )
                print(new_bullet)

                mbc, is_mbc = find_multibc(b)
                if is_mbc:
                    create_multibc(new_bullet, mbc)
            except ValueError as err:
                tb_string = traceback.format_list(traceback.extract_tb(err.__traceback__))[0]
                print(f"{tb_string} object: BulletTuple, id: {b.id}".replace('\n object', ' object'))


def find_g1_bullet_for_g7(bullets7: list[Bullet7Tuple]):
    bullets = Bullet.objects.all()

    bullets1 = {}

    for b in bullets:
        name1 = re.sub(r'\W', '', b.name.lower())
        vendor1 = re.sub(r'\W', '', b.vendor.name.lower())
        bullets1[f"{name1}{vendor1}{b.diameter.diameter}{b.weight}"] = b.id
        # print('G1', f"{name1}{vendor1}{b.diameter.diameter}{b.weight}")

    for b in bullets7:
        name7 = re.sub(r'\W', '', b.name.lower())
        vendor7 = re.sub(r'\W', '', b.vendor.lower())
        bul = f"{name7}{vendor7}{float(b.diameter)}{float(b.weight)}"

        if bul in bullets1:
            print('FOUND', bul, b.id, bullets1.get(bul))
        else:
            # print('NOT', bul)
            pass


if __name__ == '__main__':
    # # buls = get_bullets()
    # # vens = get_vendors_by_bullet(buls)
    # # add_vendors_to_db(vens)
    # # diams = get_diameters_by_bullet(buls)
    # # add_diameters_to_db(diams)
    # #
    # # add_bullets(buls)
    #
    # buls7 = get_bullets7()
    # find_g1_bullet_for_g7(buls7)

    dfs = DragFunction.objects.filter(df_type=DragFunction.DragFunctionType.G1)
    for df in dfs:
        df.df_type = DragFunction.DragFunctionType.G1_MULTI_BC
        df.save()
