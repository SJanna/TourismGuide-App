# Generated by Django 4.1.3 on 2022-11-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_place_image'),
        ('users', '0006_rename_places_myroute_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myroute',
            name='place',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='locations.place'),
        ),
    ]
