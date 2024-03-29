# Generated by Django 5.0 on 2024-01-20 17:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0081_truck'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorewellTruck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='borewelltruck_images/')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_contact', models.CharField(max_length=20)),
                ('driver_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('station', models.CharField(max_length=100)),
                ('status', models.CharField(default='Available', max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_borewelltrucks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CombineHarvester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='combineharvester_images/')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_contact', models.CharField(max_length=20)),
                ('driver_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('station', models.CharField(max_length=100)),
                ('status', models.CharField(default='Available', max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_combineharvesters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jcb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='jcb_images/')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_contact', models.CharField(max_length=20)),
                ('driver_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('station', models.CharField(max_length=100)),
                ('status', models.CharField(default='Available', max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_jcbs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(max_length=20)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='tractor_images/')),
                ('vehicle_name', models.CharField(max_length=100)),
                ('rent_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('driver_name', models.CharField(max_length=100)),
                ('driver_contact', models.CharField(max_length=20)),
                ('driver_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('station', models.CharField(max_length=100)),
                ('status', models.CharField(default='Available', max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_tractors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
