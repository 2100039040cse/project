# Generated by Django 5.0 on 2024-01-08 16:47

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0074_delete_canceledbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanceledBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vehicle_id', models.CharField(max_length=20)),
                ('vehicle_name', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('start_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.paymentdetails')),
            ],
        ),
    ]
