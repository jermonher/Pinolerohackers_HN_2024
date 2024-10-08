# Generated by Django 5.1 on 2024-09-07 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=200)),
                ('conservation_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('notes', models.TextField()),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.species')),
            ],
        ),
    ]
