# Generated by Django 4.0.3 on 2022-06-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0019_alter_clininfo_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='num_of_building',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
