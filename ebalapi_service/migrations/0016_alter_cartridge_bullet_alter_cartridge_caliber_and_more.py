# Generated by Django 4.2 on 2023-04-06 11:29

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0015_cartridge_diameter_alter_cartridge_bullet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='bullet',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='diameter', on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='ebalapi_service.bullet'),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='caliber',
            field=smart_selects.db_fields.GroupedForeignKey(default=0, group_field='diameter', on_delete=django.db.models.deletion.CASCADE, related_name='cartridges', to='ebalapi_service.caliber'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='diameter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartridges', to='ebalapi_service.diameter'),
        ),
    ]