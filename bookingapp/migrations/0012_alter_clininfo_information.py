# Generated by Django 4.0.3 on 2022-06-16 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0011_clininfo_doctor_name_clininfo_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clininfo',
            name='information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='info', to='bookingapp.clinic'),
        ),
    ]
