# Generated by Django 5.0 on 2024-01-07 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_cancellationreason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancellationreason',
            name='payment',
        ),
    ]
