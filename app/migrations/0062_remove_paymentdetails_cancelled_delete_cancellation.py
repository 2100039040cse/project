# Generated by Django 5.0 on 2024-01-07 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0061_paymentdetails_cancelled_cancellation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentdetails',
            name='cancelled',
        ),
        migrations.DeleteModel(
            name='Cancellation',
        ),
    ]
