# Generated by Django 4.2 on 2023-04-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0021_rename_drag_function_data_dragfunction_df_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletvendor',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cartridgevendor',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='riflevendor',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
