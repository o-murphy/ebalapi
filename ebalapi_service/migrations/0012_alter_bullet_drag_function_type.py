# Generated by Django 4.2 on 2023-04-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0011_cartridgevendor_cartridge_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='drag_function_type',
            field=models.IntegerField(choices=[(1, 'G1'), (2, 'G2'), (3, 'G5'), (4, 'G6'), (5, 'G7'), (6, 'G8'), (7, 'GS'), (8, 'GC'), (9, 'G1 MULTI BC'), (10, 'G7 MULTI BC'), (11, 'CUSTOM')], default=5, max_length=20),
        ),
    ]
