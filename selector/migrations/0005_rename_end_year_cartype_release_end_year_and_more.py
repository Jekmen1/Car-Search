# Generated by Django 5.1.1 on 2024-10-04 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selector', '0004_cartype_end_year_cartype_start_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartype',
            old_name='end_year',
            new_name='release_end_year',
        ),
        migrations.RenameField(
            model_name='cartype',
            old_name='start_year',
            new_name='release_start_year',
        ),
    ]