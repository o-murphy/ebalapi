# Generated by Django 4.2 on 2023-04-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0022_bulletvendor_comment_cartridgevendor_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bullet',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='bulletvendor',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='caliber',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='cartridgevendor',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='dragfunction',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='riflevendor',
            name='comment',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
    ]