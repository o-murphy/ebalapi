# Generated by Django 4.2 on 2023-04-18 07:46

from django.db import migrations
import ebalapi_service.models.search_tag


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0032_alter_dragfunction_df_data_searchtag'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='searchtag',
            managers=[
                ('content_objects', ebalapi_service.models.search_tag.ContentObjectManager()),
            ],
        ),
    ]
