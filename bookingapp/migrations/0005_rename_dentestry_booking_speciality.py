# Generated by Django 4.0.3 on 2022-05-20 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0004_alter_booking_available_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='dentestry',
            new_name='speciality',
        ),
    ]
