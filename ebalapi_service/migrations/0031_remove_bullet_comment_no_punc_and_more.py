# Generated by Django 4.2 on 2023-04-18 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebalapi_service', '0030_bullet_comment_no_punc_bullet_name_no_punc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bullet',
            name='comment_no_punc',
        ),
        migrations.RemoveField(
            model_name='bullet',
            name='name_no_punc',
        ),
    ]