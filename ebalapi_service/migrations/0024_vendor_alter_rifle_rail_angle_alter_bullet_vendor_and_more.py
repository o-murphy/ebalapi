# Generated by Django 4.2 on 2023-04-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0023_alter_bullet_comment_alter_bulletvendor_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40, unique=True)),
                ('comment', models.CharField(blank=True, max_length=280, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='rifle',
            name='rail_angle',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='bullet',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bullets', to='ebalapi_service.vendor'),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartridges', to='ebalapi_service.vendor'),
        ),
        migrations.AlterField(
            model_name='rifle',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rifles', to='ebalapi_service.vendor'),
        ),
        migrations.DeleteModel(
            name='BulletVendor',
        ),
        migrations.DeleteModel(
            name='CartridgeVendor',
        ),
        migrations.DeleteModel(
            name='RifleVendor',
        ),
    ]
