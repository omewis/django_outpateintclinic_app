# Generated by Django 4.0.3 on 2022-06-18 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0021_remove_num_of_building_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='speciality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingapp.doctor'),
        ),
    ]
