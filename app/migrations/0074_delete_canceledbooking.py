# Generated by Django 5.0 on 2024-01-08 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_canceledbooking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CanceledBooking',
        ),
    ]
