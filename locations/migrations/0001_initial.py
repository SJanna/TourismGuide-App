# Generated by Django 4.1.3 on 2022-11-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('R', 'Restaurant'), ('H', 'Hotel'), ('A', 'Attraction')], max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('coordinates', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
