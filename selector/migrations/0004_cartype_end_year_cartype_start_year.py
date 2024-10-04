# Generated by Django 5.1.1 on 2024-10-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selector', '0003_remove_cartype_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartype',
            name='end_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartype',
            name='start_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]