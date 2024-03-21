# Generated by Django 5.0.3 on 2024-03-21 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_founded', models.PositiveIntegerField()),
                ('population', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review_title', models.CharField(max_length=100)),
                ('review_description', models.TextField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.attraction')),
            ],
        ),
    ]
