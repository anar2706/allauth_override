# Generated by Django 2.2.5 on 2019-09-08 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20190908_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='iamge3',
            new_name='image3',
        ),
    ]