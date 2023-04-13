import csv
import os
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


def get_bullets() -> list[BulletTuple]:
    with open('bullets.csv', 'r') as fp:
        data = csv.reader(fp, delimiter=',')
        bullets = [BulletTuple(*row) for row in data]
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
        df_type=DragFunction.DragFunctionType.G1,
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


if __name__ == '__main__':
    buls = get_bullets()
    vens = get_vendors_by_bullet(buls)
    add_vendors_to_db(vens)
    diams = get_diameters_by_bullet(buls)
    add_diameters_to_db(diams)

    add_bullets(buls)

    # print(vens)
